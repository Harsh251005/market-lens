import yfinance as yf

from src.models import Stock


def get_stock_metadata(symbol: str) -> Stock:
    ticker = yf.Ticker(symbol)
    info = ticker.info

    return Stock(
        symbol=symbol,
        company=info.get("longName", symbol),
        sector=info.get("sector", "Unknown"),
        industry=info.get("industry", "Unknown"),
    )