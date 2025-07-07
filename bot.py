from discord import Intents, Client
from dotenv import load_dotenv
from os import getenv
import time

load_dotenv()
VOICE_CHANNEL_ID = int(getenv('VOICE_CHANNEL_ID'))
NOTIFICATION_CHANNEL_ID = int(getenv('NOTIFICATION_CHANNEL_ID'))
COOLDOWN_TIME = int(getenv('COOLDOWN_TIME'))

last_notification_time = 0

intents = Intents.default()
intents.members = True
intents.voice_states = True

client = Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')


@client.event
async def on_voice_state_update(member, before, after):
    global last_notification_time
    current_time = time.time()
    if after.channel is not None and after.channel.id == VOICE_CHANNEL_ID and len(after.channel.members) == 1 and (current_time - last_notification_time) > COOLDOWN_TIME:
        last_notification_time = current_time
        notification_channel = client.get_channel(NOTIFICATION_CHANNEL_ID)
        if notification_channel is not None:
            await notification_channel.send(f'@everyone {member.mention} has joined the {after.channel.name} voice channel.')
            print(f'{member.display_name} joined voice channel {after.channel.id}')
        else:
            print(f'Notification channel {NOTIFICATION_CHANNEL_ID} not found')

client.run(token=getenv('BOT_TOKEN'), reconnect=True)
