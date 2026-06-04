"""Получение цены TON из публичных источников без ключей."""

from __future__ import annotations

import logging

import aiohttp

import config

logger = logging.getLogger(__name__)
REQUEST_TIMEOUT = aiohttp.ClientTimeout(total=10)


async def _fetch_coingecko(session: aiohttp.ClientSession) -> float:
    coin_id = "the-open-network"
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd"}
    async with session.get(url, params=params, timeout=REQUEST_TIMEOUT) as resp:
        resp.raise_for_status()
        data = await resp.json()
        return float(data[coin_id]["usd"])


async def _fetch_binance(session: aiohttp.ClientSession) -> float:
    symbol = f"{config.API_TICKER.upper()}USDT"
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": symbol}
    async with session.get(url, params=params, timeout=REQUEST_TIMEOUT) as resp:
        resp.raise_for_status()
        data = await resp.json()
        return float(data["price"])


async def _fetch_okx(session: aiohttp.ClientSession) -> float:
    inst_id = f"{config.API_TICKER.upper()}-USDT"
    url = "https://www.okx.com/api/v5/market/ticker"
    params = {"instId": inst_id}
    async with session.get(url, params=params, timeout=REQUEST_TIMEOUT) as resp:
        resp.raise_for_status()
        data = await resp.json()
        return float(data["data"][0]["last"])


async def _fetch_bybit(session: aiohttp.ClientSession) -> float:
    symbol = f"{config.API_TICKER.upper()}USDT"
    url = "https://api.bybit.com/v5/market/tickers"
    params = {"category": "spot", "symbol": symbol}
    async with session.get(url, params=params, timeout=REQUEST_TIMEOUT) as resp:
        resp.raise_for_status()
        data = await resp.json()
        return float(data["result"]["list"][0]["lastPrice"])


async def _fetch_dexscreener(session: aiohttp.ClientSession) -> float:
    url = f"https://api.dexscreener.com/latest/dex/search?q={config.API_TICKER.upper()}"
    async with session.get(url, timeout=REQUEST_TIMEOUT) as resp:
        resp.raise_for_status()
        data = await resp.json()
        pairs = data.get("pairs") or []
        for pair in pairs:
            price_usd = pair.get("priceUsd")
            if price_usd:
                return float(price_usd)
    raise ValueError("DexScreener: цена в USD не найдена")


SOURCES = [
    ("CoinGecko", _fetch_coingecko),
    ("Binance", _fetch_binance),
    ("OKX", _fetch_okx),
    ("Bybit", _fetch_bybit),
    ("DexScreener", _fetch_dexscreener),
]


async def get_price() -> float | None:
    async with aiohttp.ClientSession() as session:
        for name, fetcher in SOURCES:
            try:
                price = await fetcher(session)
                logger.info("Цена TON из %s: %s", name, price)
                return price
            except Exception as exc:  # noqa: BLE001
                logger.warning("Источник %s недоступен: %s", name, exc)
    logger.error("Не удалось получить цену TON ни из одного источника")
    return None


def format_price(price: float) -> str:
    return f"{price:.2f}"
