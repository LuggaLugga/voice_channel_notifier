import time
from discord import Client, Intents
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

BOT_TOKEN = config['bot']['token']
COOLDOWN_TIME = int(config['bot']['cooldown'])
CHANNEL_MAPPING = {
    int(voice_channel): [int(text_channel) for text_channel in targets]
    for voice_channel, targets in config['channel_mapping'].items()
}

last_notification_time = {voice_channel: 0 for voice_channel in CHANNEL_MAPPING}

intents = Intents.default()
intents.members = True
intents.voice_states = True
client = Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')


@client.event
async def on_voice_state_update(member, before, after):

    if not after.channel or after.channel.id not in CHANNEL_MAPPING:
        return

    if len(after.channel.members) != 1:
        return

    now = time.time()
    voice_channel_id = after.channel.id

    if now - last_notification_time[voice_channel_id] <= COOLDOWN_TIME:
        return

    last_notification_time[voice_channel_id] = now

    for notification_channel_id in CHANNEL_MAPPING[voice_channel_id]:

        notification_channel = client.get_channel(notification_channel_id)

        if notification_channel:
            await notification_channel.send(f'@everyone {member.mention} has joined the {after.channel.name} voice '
                                            f'channel.')
            print(f'{member.display_name} joined voice channel {after.channel.id}')
        else:
            print(f'Notification channel {notification_channel_id} not found')

client.run(token=BOT_TOKEN, reconnect=True)
