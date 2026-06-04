"""Load configuration from .env file and environment variables."""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


def _parse_chat_id(value: str) -> int | str:
    """Parse chat ID as int if numeric, otherwise keep as string."""
    if value and value.lstrip("-").isdigit():
        return int(value)
    return value


BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_ID = _parse_chat_id(os.getenv("CHANNEL_ID", ""))
API_TICKER = os.getenv("API_TICKER", "TON")
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", "60"))
