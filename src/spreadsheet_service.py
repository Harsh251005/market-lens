from src.config import (
    GOOGLE_CREDENTIALS_FILE,
    SPREADSHEET_ID,
)
from src.models import Stock

import gspread
from gspread import Spreadsheet, Worksheet
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


class SpreadsheetService:
    def __init__(self, spreadsheet_id: str):
        credentials = Credentials.from_service_account_file(
            GOOGLE_CREDENTIALS_FILE,
            scopes=SCOPES,
        )

        client = gspread.authorize(credentials)
        self.spreadsheet: Spreadsheet = client.open_by_key(spreadsheet_id)

    def get_or_create_sheet(self, sheet_name: str) -> Worksheet:
        try:
            return self.spreadsheet.worksheet(sheet_name)
        except gspread.WorksheetNotFound:
            return self.spreadsheet.add_worksheet(
                title=sheet_name,
                rows=1000,
                cols=20,
            )

    def write_sector(self, sector: str, stocks: list[Stock]) -> None:
        worksheet = self.get_or_create_sheet(sector)

        rows = [
            [
                "Symbol",
                "Company",
                "Industry",
                "Current Price",
                "Previous Close",
                "Open",
                "High",
                "Low",
                "Volume",
            ]
        ]

        for stock in stocks:
            rows.append([
                stock.symbol,
                stock.company,
                stock.industry,
                stock.current_price,
                stock.previous_close,
                stock.open_price,
                stock.day_high,
                stock.day_low,
                stock.volume,
            ])

        worksheet.clear()
        worksheet.update(rows)