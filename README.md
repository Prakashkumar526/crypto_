# Cryptocurrency Market Updates API

This is an HTTP REST API that fetches cryptocurrency market updates from the CoinGecko API.

## Endpoints

- `/coins`: List all coins.
- `/categories`: List coin categories.
- `/coins/{coin_id}`: Get specific coin details.

## Authentication

The application is protected with Basic Authentication.

## Running the API

```sh
docker build -t crypto-api .
docker run -d -p 8000:8000 --env USERNAME=admin --env PASSWORD=admin crypto-api
```
