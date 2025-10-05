from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Dict
from pydantic import BaseModel, RootModel


class PairQuote(BaseModel):
    code: str
    codein: str
    name: str
    high: Decimal
    low: Decimal
    varBid: Decimal
    pctChange: Decimal
    bid: Decimal
    ask: Decimal
    timestamp: int          
    create_date: datetime    

class QuoteMap(RootModel[Dict[str, PairQuote]]):
    pass
