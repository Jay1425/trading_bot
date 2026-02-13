import argparse
import os
import logging
from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def main():
    """Main entry point for the trading bot CLI."""
    setup_logging()
    
    # Log startup information
    logger.info("="*60)
    logger.info("Trading Bot Started")
    logger.info("Exchange: Binance Futures Testnet")
    logger.info("Endpoint: https://testnet.binancefuture.com")
    logger.info("="*60)

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot - Place orders on testnet"
    )
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Order price (required for LIMIT orders)")

    args = parser.parse_args()

    # Validate API credentials
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not api_secret:
        raise EnvironmentError(
            "❌ Missing API credentials. Please set BINANCE_API_KEY "
            "and BINANCE_SECRET_KEY in .env file"
        )

    # Validate inputs
    symbol = validate_symbol(args.symbol)
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)

    price = None
    if order_type == "LIMIT":
        if not args.price:
            raise ValueError("❌ LIMIT order requires --price parameter")
        price = validate_price(args.price)

    client = BinanceFuturesClient(
        api_key=api_key,
        api_secret=api_secret
    )

    response = place_order(
        client,
        symbol,
        side,
        order_type,
        quantity,
        price
    )

    # Display order summary
    print("\n" + "="*50)
    print("           ORDER SUMMARY")
    print("="*50)
    print(f"Symbol:        {symbol}")
    print(f"Side:          {side}")
    print(f"Type:          {order_type}")
    print(f"Quantity:      {quantity}")
    if price:
        print(f"Price:         {price}")

    print("\n" + "="*50)
    print("           EXCHANGE RESPONSE")
    print("="*50)
    print(f"Order ID:      {response.get('orderId')}")
    print(f"Status:        {response.get('status')}")
    print(f"Executed Qty:  {response.get('executedQty')}")
    print(f"Avg Price:     {response.get('avgPrice', 'N/A')}")
    print("="*50)
    
    if response.get("status") in ["NEW", "FILLED"]:
        print("\n✅ Order accepted by exchange.")
    else:
        print("\n⚠ Order not accepted.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"\n❌ Validation Error: {e}")
        exit(1)
    except EnvironmentError as e:
        print(f"\n{e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        print("Check logs/trading.log for details.")
        exit(1)
