import json
from pathlib import Path

import yfinance as yf

from src.config import METADATA_CACHE_FILE
from src.models import Stock

CACHE_FILE = Path(METADATA_CACHE_FILE)


def _load_cache() -> dict:
    if not CACHE_FILE.exists():
        return {}

    with CACHE_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def _save_cache(cache: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with CACHE_FILE.open("w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)


def get_stock_metadata(symbol: str) -> Stock:
    cache = _load_cache()

    if symbol in cache:
        return Stock(**cache[symbol])

    ticker = yf.Ticker(symbol)
    info = ticker.info

    stock = Stock(
        symbol=symbol,
        company=info.get("longName", symbol),
        sector=info.get("sector", "Unknown"),
        industry=info.get("industry", "Unknown"),
    )

    cache[symbol] = stock.model_dump()
    _save_cache(cache)

    return stock