from pydantic import BaseModel
from typing import List

class Coin(BaseModel):
    id: str
    name: str
    symbol: str
    current_price: float

class CoinCategory(BaseModel):
    category: str
    coins: List[Coin]
