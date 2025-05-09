# py-nobitex-api

**Python client for the Nobitex cryptocurrency exchange API**

This package provides a clean, class-based interface to the Nobitex REST API, including methods for authentication, market data retrieval, order management, and wallet balance checks.

---

## Features

* **Authentication**: Secure login and token management
* **Market Data**: Fetch current market statistics (best buy/sell prices)
* **Wallets**: Retrieve your account balances for all currencies
* **Order Management**: Place, cancel, and list user orders
* **Error Handling**: Raises exceptions on API errors for robust integration

<br>

## Installation

```bash
pip install py-nobitex-api
```

Or install with git (should have git installed):

```bash
pip install https://github.com/HMohammad2520/py-nobitex-api.git
```

<br>

## Quick Start

- authenticate with username or password: ***#OTP NOT IMPLEMENTED YET***
```python
from nobitex_api.client import NobitexClient

client = NobitexClient(username="you@example.com", password="your_password")
client.Auth.login()
```

- Or provide the token:
```python
from nobitex_api.client import NobitexClient

client = NobitexClient(token='YOUR_TOKEN_HERE')
```
- Simple code example:
```python
from nobitex_api import NobitexClient
from nobitex_api import CurrencyManager as CM
from config import token
from pprint import pprint

# Create a new client
clinet = NobitexClient(token=token)

# Get the current price of BTC
btc_stats = clinet.Market.get_stats(
    src_currency=CM.btc, # Use Currency manager for smother usage
    dst_currency=CM.rial,
    )

# Print the result
pprint(btc_stats)
```

### Testing

You can test your scripts with the testing platform of nobitex:

```python
# Import the test url
from nobitex_api.client import NobitexClient, TestNobitexAPI

client = NobitexClient(api_url=TestNobitexAPI ,token='YOUR_TOKEN_HERE')
```
<br>

## Missing / Upcoming Endpoints

- users (Not all of routes are implemented)
- liquidity-pools
- margin
- positions
- withdraws
- address_book

<br>

## Contribution

Feel free to contribute or request additional endpoints!

Happy trading! 🚀
