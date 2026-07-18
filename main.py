from collections import defaultdict

from src.market_service import get_market_data


def main():
    grouped = defaultdict(list)

    stocks = get_market_data()

    for stock in stocks:
        grouped[stock.sector].append(stock)

    for sector, sector_stocks in grouped.items():
        print(f"\n=== {sector} ===")

        for stock in sector_stocks:
            print(
                f"{stock.symbol:<15}"
                f"{stock.current_price}"
            )


if __name__ == "__main__":
    main()