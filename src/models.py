from pydantic import BaseModel


class Stock(BaseModel):
    symbol: str
    company: str
    sector: str
    industry: str