from collections import defaultdict

from src.market_service import get_market_data
from src.spreadsheet_service import SpreadsheetService


class SyncService:
    def __init__(self, spreadsheet: SpreadsheetService):
        self.spreadsheet = spreadsheet

    def sync(self) -> None:
        grouped = defaultdict(list)

        for stock in get_market_data():
            grouped[stock.sector].append(stock)

        for sector in sorted(grouped):
            worksheet = self.spreadsheet.get_or_create_sheet(sector)

            # Create headers if the sheet is empty
            if not worksheet.get_all_values():
                worksheet.append_row([
                    "Symbol",
                    "Company",
                    "Industry",
                    "Current Price",
                    "Previous Close",
                    "Open",
                    "High",
                    "Low",
                    "Volume",
                ])

            symbol_map = self.spreadsheet.get_symbol_row_map(worksheet)

            for stock in grouped[sector]:
                if stock.symbol in symbol_map:
                    self.spreadsheet.update_stock(
                        worksheet,
                        symbol_map[stock.symbol],
                        stock,
                    )
                else:
                    self.spreadsheet.append_stock(
                        worksheet,
                        stock,
                    )

            print(f"✓ Updated {sector}")