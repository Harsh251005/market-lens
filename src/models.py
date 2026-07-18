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