# Pennyworth
Multi-Purpose Discord Bot

## Setup

### Discord Developer Portal
TODO

### Python
Instructions made with Void Linux in mind.

1. sudo xbps-install python3
1. sudo xbps-install python3-pip
1. pip install -U discord.py
1. pip install -U python-dotenv

### Application
Create the file `pennyworth/.env` and configure the following variables:
DISCORD_TOKEN={your-bot-token}
DISCORD_GUILD={your-guild-name}

## Run

```bash
python pennyworth/pennyworth.py
```