from collections import defaultdict

from src.config import SPREADSHEET_ID
from src.market_service import get_market_data
from src.spreadsheet_service import SpreadsheetService


def main():
    spreadsheet = SpreadsheetService(SPREADSHEET_ID)

    grouped = defaultdict(list)

    for stock in get_market_data():
        grouped[stock.sector].append(stock)

    for sector, stocks in grouped.items():
        spreadsheet.write_sector(sector, stocks)
        print(f"Updated {sector}")


if __name__ == "__main__":
    main()