"""Бот-бот, который публикует цену TON в Telegram канал каждую минуту."""

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
logger = logging.getLogger("ton-price-bot")


def build_message(price: float) -> str:
    """Формируем текст поста с ценой TON."""
    return f"TON: {format_price(price)} USD"


async def publish_loop(bot: Bot) -> None:
    """Публикация цены в канал с интервалом из настроек."""
    while True:
        try:
            price = await get_price()
            if price is not None:
                text = build_message(price)
                await bot.send_message(chat_id=config.CHANNEL_ID, text=text)
                logger.info("Опубликовано: %s", text)
            else:
                logger.warning("Цена не получена — пропускаем итерацию")
        except Exception as exc:  # noqa: BLE001
            logger.exception("Ошибка при публикации: %s", exc)

        await asyncio.sleep(config.UPDATE_INTERVAL)


async def main() -> None:
    if not config.BOT_TOKEN or not config.CHANNEL_ID:
        raise RuntimeError("BOT_TOKEN и CHANNEL_ID должны быть заданы в файле .env")

    bot = Bot(token=config.BOT_TOKEN)
    logger.info("Запуск трекера TON price. Интервал: %s сек.", config.UPDATE_INTERVAL)
    try:
        await publish_loop(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
