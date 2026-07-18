from collections import defaultdict

from src.market_service import get_market_data
from src.spreadsheet_service import SpreadsheetService


class SyncService:
    def __init__(self, spreadsheet: SpreadsheetService):
        self.spreadsheet = spreadsheet

    def sync(self) -> None:
        grouped = defaultdict(list)

        stocks = get_market_data()

        for stock in stocks:
            grouped[stock.sector].append(stock)

        for sector in sorted(grouped):
            self.spreadsheet.write_sector(
                sector,
                grouped[sector],
            )

            print(f"✓ Updated {sector}")