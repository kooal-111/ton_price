# TON Price Tracker

Публикует цену TON в Telegram-канал каждую минуту, используя только публичные API без встроенных ключей.

## Возможности

- публикует цену TON в канал Telegram
- обновляет данные каждую минуту (или по настройке `UPDATE_INTERVAL`)
- использует резервные источники данных
- конфигурация хранится во внешнем `.env`, ключи не жестко закодированы

## Требования

- Python 3.11+
- `aiogram`
- `aiohttp`
- `python-dotenv`

## Установка

1. Создайте виртуальное окружение:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Установите зависимости:
   ```powershell
   pip install -r requirements.txt
   ```
3. Скопируйте шаблон `.env.example` в `.env` и заполните параметры:
   ```powershell
   copy .env.example .env
   ```

## Настройка

В файле `.env` задайте:
- `BOT_TOKEN` — токен Telegram-бота
- `CHANNEL_ID` — id канала или username в формате `@channelname`
- `UPDATE_INTERVAL` — интервал публикации в секундах (по умолчанию `60`)
- `API_TICKER` — тикер монеты (по умолчанию `TON`)

## Запуск

```powershell
python bot.py
```

## Docker (опционально)

Если хотите запускать в контейнере, можно добавить свою `Dockerfile` и `docker-compose.yml`.

## Структура

- `bot.py` — основной цикл публикации в Telegram
- `price_fetcher.py` — получение цены из публичных API
- `config.py` — загрузка настроек из `.env`
- `requirements.txt` — зависимости

## Вклад

См. [CONTRIBUTING.md](CONTRIBUTING.md).

## Лицензия

Проект распространяется под лицензией MIT. См. файл `LICENSE`.
