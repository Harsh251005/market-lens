from pydantic import BaseModel


class Stock(BaseModel):
    symbol: str
    company: str
    sector: str
    industry: str

    current_price: float | None = None
    previous_close: float | None = None
    open_price: float | None = None
    day_high: float | None = None
    day_low: float | None = None
    volume: int | None = None

    market_cap: float | None = None
    pe_ratio: float | None = None
    eps: float | None = None
    dividend_yield: float | None = None
    currency: str | None = None
    exchange: str | None = None