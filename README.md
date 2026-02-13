# Binance Futures Trading Bot

A command-line trading bot for placing orders on Binance Futures testnet. This bot allows you to execute market and limit orders with proper validation and logging.

## Features

- 🚀 Place MARKET and LIMIT orders
- 📊 Support for BUY and SELL operations
- ✅ Input validation for all order parameters
- 📝 Comprehensive logging of all orders
- 🔐 Secure API key management with environment variables
- 🧪 Testnet integration for risk-free testing
- 🧱 Modular and reusable architecture

## Project Structure

```
trading_bot/
├── cli.py                  # Main CLI entry point
├── requirements.txt        # Python dependencies
├── .env                    # API credentials (not tracked)
├── bot/
│   ├── client.py          # Binance Futures API client
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation functions
│   └── logging_config.py  # Logging configuration
└── logs/
    └── trading.log        # Order history and logs
```

The architecture separates CLI, business logic, and API client layers to ensure modularity, testability, and maintainability.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd trading_bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key
```

## Getting Testnet Credentials

1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com/)
2. Sign up or log in
3. Generate API keys from your account settings
4. Add the keys to your `.env` file

**Base URL used:** `https://testnet.binancefuture.com`

## Usage

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
```

### Command-Line Arguments

- `--symbol`: Trading pair symbol (e.g., BTCUSDT, ETHUSDT)
- `--side`: Order side - BUY or SELL
- `--type`: Order type - MARKET or LIMIT
- `--quantity`: Order quantity (must be positive)
- `--price`: Order price (required for LIMIT orders)

## Examples

**Buy Bitcoin at Market Price:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

**Sell Ethereum with Limit Order:**
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.05 --price 3000
```

## Logging

All order requests and responses are logged to `logs/trading.log`. Each log entry includes:
- Timestamp
- Order parameters
- API response
- Error messages (if any)

## Validation

The bot validates all inputs before placing orders:
- ✓ Side must be BUY or SELL
- ✓ Type must be MARKET or LIMIT
- ✓ Quantity must be positive
- ✓ Price must be positive (for LIMIT orders)
- ✓ LIMIT orders require a price parameter

## Security Notes

- Never commit your `.env` file
- Use testnet for testing before going live
- Keep your API keys secure
- The bot uses testnet endpoint by default

## Error Handling

The bot includes comprehensive error handling:
- Invalid inputs are caught and reported
- API errors are logged with full details
- Exceptions are handled gracefully without terminating the application

## Dependencies

- `python-binance`: Binance API wrapper
- `python-dotenv`: Environment variable management

## Assumptions

This trading bot operates under the following assumptions:

1. **Testnet Environment**: All orders are placed on Binance Futures testnet, not production
2. **Minimum Notional**: Orders must meet the 100 USDT minimum notional value requirement
3. **Symbol Format**: Trading pairs follow Binance format (e.g., BTCUSDT, ETHUSDT)
4. **Network Connectivity**: Stable internet connection for API communication
5. **API Rate Limits**: User is responsible for staying within Binance API rate limits
6. **Position Mode**: The bot assumes "One-Way" position mode (BOTH position side)
7. **Leverage**: Default leverage settings from Binance account are used
8. **Time In Force**: LIMIT orders use GTC (Good Till Cancelled) by default

## Log File Sample Explanation

The bot logs all activity to `logs/trading.log` with the following format:

```
2026-02-13 16:55:51,712 | INFO | bot.orders | Notional Value: 197.28 USDT (Current Price: 98640.0)
2026-02-13 16:55:51,712 | INFO | bot.orders | Order Request: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.002}
2026-02-13 16:55:52,646 | INFO | bot.orders | Order Response: {'orderId': 12241303472, 'symbol': 'BTCUSDT', 'status': 'NEW', ...}
```

**Log Entry Components:**
- **Timestamp**: When the action occurred (format: YYYY-MM-DD HH:MM:SS,mmm)
- **Level**: Log severity (INFO, ERROR, WARNING)
- **Module**: Source module that generated the log (e.g., bot.orders, bot.client)
- **Message**: Detailed information about the action

**Key Log Events:**
- **Notional Value**: Shows calculated order value and current market price
- **Order Request**: Parameters sent to Binance API
- **Order Response**: Complete response from exchange including order ID, status, and execution details
- **Errors**: Any exceptions or validation failures with stack traces

Use logs for:
- Debugging failed orders
- Tracking order history
- Auditing trading activity
- Analyzing execution prices

## Future Improvements

- Add retry mechanism with exponential backoff
- Implement order status polling
- Add support for Stop-Market and OCO orders
- Integrate risk management rules
- Add unit tests
- Add async support for higher throughput

## License

MIT License

## Disclaimer

This bot is for educational purposes. Use at your own risk. Always test on testnet before using real funds.
