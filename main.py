from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import requests
import os
from typing import List

app = FastAPI()

# Authentication
security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = os.getenv("USERNAME", "admin")
    correct_password = os.getenv("PASSWORD", "admin")
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Models
class Coin(BaseModel):
    id: str
    name: str
    symbol: str
    current_price: float

class CoinCategory(BaseModel):
    category: str
    coins: List[Coin]

# Utility functions
def fetch_coins():
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad")
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coins not found")

def fetch_coin_categories():
    response = requests.get("https://api.coingecko.com/api/v3/coins/categories")
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coin categories not found")

@app.get("/coins", response_model=List[Coin])
def list_coins(page_num: int = 1, per_page: int = 10, current_user: str = Depends(get_current_user)):
    coins = fetch_coins()
    start = (page_num - 1) * per_page
    end = start + per_page
    return coins[start:end]

@app.get("/categories", response_model=List[CoinCategory])
def list_categories(current_user: str = Depends(get_current_user)):
    categories = fetch_coin_categories()
    return categories

@app.get("/coins/{coin_id}", response_model=Coin)
def get_coin(coin_id: str, current_user: str = Depends(get_current_user)):
    coins = fetch_coins()
    for coin in coins:
        if coin['id'] == coin_id:
            return coin
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coin not found")
