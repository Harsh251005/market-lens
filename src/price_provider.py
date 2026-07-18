import yfinance as yf


def get_live_prices(symbols: list[str]):
    data = yf.download(
        tickers=symbols,
        period="1d",
        interval="1m",
        group_by="ticker",
        auto_adjust=False,
        progress=False,
        threads=True,
    )

    return data