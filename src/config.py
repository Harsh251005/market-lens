from pathlib import Path

UPDATE_INTERVAL_MINUTES = 5

METADATA_CACHE_FILE = "data/metadata.json"

YFINANCE_PERIOD = "1d"
YFINANCE_INTERVAL = "1m"

ROOT_PATH = Path(__file__).resolve().parents[1]

GOOGLE_CREDENTIALS_FILE = ROOT_PATH / "credentials/service_account.json"
SPREADSHEET_ID = "1Nqv1aNIZQdFj941z21zrztxvf3_fyXlsfFE1sKjjtmg"