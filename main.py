from collections import defaultdict

from src.watchlist import WATCHLIST
from src.yahoo_provider import get_stock_metadata


def main():
    grouped = defaultdict(list)

    for symbol in WATCHLIST:
        stock = get_stock_metadata(symbol)
        grouped[stock.sector].append(stock)

    for sector, stocks in grouped.items():
        print(f"\n=== {sector} ===")
        for stock in stocks:
            print(f"{stock.symbol} - {stock.company}")


if __name__ == "__main__":
    main()