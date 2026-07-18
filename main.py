from collections import defaultdict

from src.price_provider import get_live_prices
from src.watchlist import WATCHLIST
from src.yahoo_provider import get_stock_metadata


def main():
    grouped = defaultdict(list)

    for symbol in WATCHLIST:
        stock = get_stock_metadata(symbol)
        grouped[stock.sector].append(stock)

    prices = get_live_prices(WATCHLIST)

    print(prices.head())

    for sector, stocks in grouped.items():
        print(f"\n=== {sector} ===")
        for stock in stocks:
            print(stock.symbol)


if __name__ == "__main__":
    main()