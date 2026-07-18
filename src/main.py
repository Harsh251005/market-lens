from src.config import SPREADSHEET_ID
from src.spreadsheet_service import SpreadsheetService

service = SpreadsheetService(SPREADSHEET_ID)

sheet = service.get_or_create_sheet("Technology")

print(sheet.title)