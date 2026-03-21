# Docker Status Bot [Telegram API]

![DockerBot](https://github.com/wpxq/DockerTelegramBot/blob/main/dockerbot.png)

---

Docker Bot for Telegram that uses a command to list which containers are running and which are not

---

## Features
### `/status`
* list running/not running Docker containers

### Requirements
* Python 3.11 or higher
* `python-telegram-bot` & `asyncio` & `colorama` libraries
* **Docker & Docker Compose** (Optional, but recommended)

## Setup
### Option 1: Docker (Recommended)
1. Create your 'config.json' from the example
2. Run the bot in the background:
   ```bash
   docker compose up -d
   ```
### Option 2: Manual
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the bot:
   ```bash
   python main.py
   ```
### Configuration (config.json)
* Make sure to fill in your `token`, `chatid`, This file is ignored by security.