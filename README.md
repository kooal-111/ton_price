# TON Price Tracker

Publishes TON price to a Telegram channel every minute using only public APIs without hardcoded keys.

## 🚀 Quick Start

```bash
git clone https://github.com/kooal-111/ton_price.git
cd ton_price
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your BOT_TOKEN and CHANNEL_ID
python bot.py
```

## ✨ Features

- ✅ Real-time TON price tracking
- ✅ Automatic Telegram posting (1-minute interval)
- ✅ Multiple fallback data sources
- ✅ No hardcoded API keys — secure by design
- ✅ Lightweight and efficient (low CPU/memory usage)
- ✅ Error handling with automatic retries

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

## 📊 Data Sources

The tracker tries these sources in order:
1. **CoinGecko** — Decentralized, no authentication required
2. **Binance** — Major exchange, high liquidity
3. **OKX** — Global trading platform
4. **Bybit** — Crypto-focused exchange
5. **DexScreener** — DEX aggregator for on-chain prices

If one source fails, it automatically falls back to the next one.

## 💡 Use Cases

- Monitor TON price in a public channel
- Set up price tracking for trading decisions
- Community price reference channel
- Integration with other trading bots

## 🔧 Troubleshooting

**Bot doesn't post?**
- Check `BOT_TOKEN` is valid in `.env`
- Verify bot has permissions in the channel
- Check logs for error messages

**Price seems wrong?**
- Multiple sources are checked — usually accurate within 1-2%
- Try checking one of the sources directly
- Verify the coin ticker is correct

## 📈 Performance

- Memory usage: ~50-100 MB
- CPU: Minimal (only active when posting)
- Network: ~1 request per minute
- Works 24/7 with proper error handling
- Tested with Python 3.11+

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
