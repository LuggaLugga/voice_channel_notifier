# Voice Channel Notifier

The Voice Channel Notifier is a bot that sends a message to a designated text channel to notify you when someone joins 
an empty voice channel, eagerly waiting for you to keep them company.

## Required privileged gateway intents

- Server members intents

## Required bot permissions

- Send messages

## Required Software

- Python 3.13 or major

## Setup and Launch

1. Navigate into the root directory of this project
2. Create a virtual environment `python3 -m venv .venv`
3. Activate the virtual environment `source .venv/bin/activate`
4. Install necessary packages `pip install -r requirements.txt`
5. Create an `config.yaml` file in the root directory according to the following pattern and define the values
    ```yaml
    bot:
      token: "<Your bot token>"
      cooldown: <Cooldown in seconds>
    channel_mapping:
      "<Voice Channel ID>":
        - "<Text Channel ID>"
        - "<Text Channel ID>"
        - "<Text Channel ID>"
      "<Voice Channel ID>":
        - "<Text Channel ID>"
        - "<Text Channel ID>"
    ```
6. Launch the bot `python bot.py`
