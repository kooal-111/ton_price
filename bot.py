"""TON Price Tracker Bot - Publishes TON price to Telegram channel every minute."""

from __future__ import annotations

import asyncio
import logging

from aiogram import Bot

import config
from price_fetcher import format_price, get_price

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("ton_price_bot")


def build_message(price: float) -> str:
    """Build the message text with TON price."""
    return f"TON: {format_price(price)} USD"


async def publish_loop(bot: Bot) -> None:
    """Publish price to channel at configured interval."""
    while True:
        try:
            price = await get_price()
            if price is not None:
                text = build_message(price)
                await bot.send_message(chat_id=config.CHANNEL_ID, text=text)
                logger.info("Published: %s", text)
            else:
                logger.warning("Price not available - skipping iteration")
        except Exception as exc:  # noqa: BLE001
            logger.exception("Publishing error: %s", exc)

        await asyncio.sleep(config.UPDATE_INTERVAL)


async def main() -> None:
    if not config.BOT_TOKEN or not config.CHANNEL_ID:
        raise RuntimeError("BOT_TOKEN and CHANNEL_ID must be set in .env file")

    bot = Bot(token=config.BOT_TOKEN)
    logger.info("Starting TON price tracker. Update interval: %s sec.", config.UPDATE_INTERVAL)
    try:
        await publish_loop(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
