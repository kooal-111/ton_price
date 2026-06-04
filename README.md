# TON Price Tracker

Publishes TON price to a Telegram channel every minute using only public APIs without hardcoded keys.

## Features

- Publishes TON price to Telegram channel
- Updates data every minute (or per `UPDATE_INTERVAL` setting)
- Uses fallback data sources for reliability
- Configuration stored externally in `.env`, no hardcoded secrets

## Requirements

- Python 3.11+
- `aiogram`
- `aiohttp`
- `python-dotenv`

## Installation

1. Create a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in the parameters:
   ```powershell
   copy .env.example .env
   ```

## Configuration

In the `.env` file, set:
- `BOT_TOKEN` — Telegram bot token
- `CHANNEL_ID` — channel ID or username in format `@channelname`
- `UPDATE_INTERVAL` — publishing interval in seconds (default `60`)
- `API_TICKER` — coin ticker (default `TON`)

## Usage

```powershell
python bot.py
```

## Docker (Optional)

You can add your own `Dockerfile` and `docker-compose.yml` for containerized deployment.

## Project Structure

- `bot.py` — main Telegram publishing loop
- `price_fetcher.py` — price fetching from public APIs
- `config.py` — configuration loading from `.env`
- `requirements.txt` — dependencies

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
