# MarketLens: a stock watchlist that keeps itself up to date in Google Sheets

![Python 3.12](https://img.shields.io/badge/python-3.12-3776AB)
![yfinance](https://img.shields.io/badge/data-yfinance-6001D2)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

Pulls live prices for a watchlist of NSE stocks and writes them into a
Google Sheet, one tab per sector. Run it again and it updates the existing
rows in place instead of rewriting the sheet, so your own notes and
formatting in other columns stay put.

## How it works

```
watchlist.py ─► yahoo_provider  ── company, sector, industry, market cap, P/E, EPS
                (cached in data/metadata.json, so it's fetched once per symbol)
            ─► price_provider   ── today's 1-minute bars in one batched yfinance call
            ─► market_service   ── current, previous, open, high, low, volume
            ─► sync_service     ── group by sector ─► one tab per sector
                                   update rows that exist, append new symbols
```

`spreadsheet_service.py` wraps gspread: it creates missing tabs and header
rows and maps each symbol to its row so only the price columns (D to I) are
rewritten.

## Run it

Requires Python 3.12+, [uv](https://docs.astral.sh/uv/) and a Google Cloud
service account with the Sheets API enabled.

```bash
git clone https://github.com/Harsh251005/market-lens.git
cd market-lens
uv sync
cp .env.example .env      # SPREADSHEET_ID
```

1. Save the service-account key as `credentials/service_account.json`.
2. Share your spreadsheet with the service account's email (Editor).
3. Edit `src/watchlist.py` to list your symbols (Yahoo Finance format,
   e.g. `RELIANCE.NS`).
4. `uv run python main.py`

## Stack

Python 3.12, yfinance, pandas, gspread, Pydantic, uv.

## Status

Runs one sync per call. Next: a scheduler for the 5-minute refresh already
set in `config.py`, and writing the cached fundamentals (market cap, P/E,
EPS) into the sheet.
