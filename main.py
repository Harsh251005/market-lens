from src.config import SPREADSHEET_ID
from src.spreadsheet_service import SpreadsheetService
from src.sync_service import SyncService


def main():
    spreadsheet = SpreadsheetService(SPREADSHEET_ID)
    sync_service = SyncService(spreadsheet)

    sync_service.sync()


if __name__ == "__main__":
    main()