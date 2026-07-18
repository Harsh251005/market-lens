import yfinance as yf

from src.config import YFINANCE_INTERVAL, YFINANCE_PERIOD


def get_live_prices(symbols: list[str]):
    return yf.download(
        tickers=symbols,
        period=YFINANCE_PERIOD,
        interval=YFINANCE_INTERVAL,
        group_by="ticker",
        auto_adjust=False,
        progress=False,
        threads=True,
    )