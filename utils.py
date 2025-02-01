import requests
from fastapi import HTTPException, status

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
