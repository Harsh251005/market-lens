from src.price_provider import get_live_prices
from src.watchlist import WATCHLIST
from src.yahoo_provider import get_stock_metadata


def get_market_data():
    stocks = [get_stock_metadata(symbol) for symbol in WATCHLIST]

    price_df = get_live_prices(WATCHLIST)

    for stock in stocks:
        try:
            row = price_df[stock.symbol]

            stock.current_price = float(row["Close"].iloc[-1])
            stock.previous_close = float(row["Close"].iloc[0])
            stock.open_price = float(row["Open"].iloc[-1])
            stock.day_high = float(row["High"].max())
            stock.day_low = float(row["Low"].min())
            stock.volume = int(row["Volume"].sum())

        except Exception:
            # Ignore failed symbols for now
            pass

    return stocks