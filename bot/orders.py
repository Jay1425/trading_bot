import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


def place_order(
    client,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: Optional[float] = None
) -> Dict[str, Any]:
    """
    Place an order on Binance Futures testnet.
    
    Args:
        client: BinanceFuturesClient instance
        symbol: Trading pair symbol (e.g., 'BTCUSDT')
        side: Order side ('BUY' or 'SELL')
        order_type: Order type ('MARKET' or 'LIMIT')
        quantity: Order quantity in base currency
        price: Limit price (required for LIMIT orders only)
    
    Returns:
        dict: Order response from Binance API containing order details
    
    Raises:
        ValueError: If notional value is below 100 USDT minimum
        Exception: If API call fails or returns an error
    """
    try:
        # Get current market price for notional validation
        ticker = client.client.futures_symbol_ticker(symbol=symbol)
        current_price = float(ticker["price"])
        
        # Calculate notional value (order value in USDT)
        notional = quantity * current_price
        
        # Validate minimum notional value
        if notional < 100:
            raise ValueError(
                f"Order notional {notional:.2f} USDT is below minimum 100 USDT"
            )
        
        logger.info(f"Notional Value: {notional:.2f} USDT (Current Price: {current_price})")
        
        order_data = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            order_data["price"] = price
            order_data["timeInForce"] = "GTC"

        logger.info(f"Order Request: {order_data}")

        response = client.create_order(**order_data)

        logger.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error placing order: {e}")
        raise
