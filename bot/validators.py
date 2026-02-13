def validate_symbol(symbol: str) -> str:
    """
    Validate trading pair symbol format.
    
    Args:
        symbol: Trading pair symbol (e.g., 'BTCUSDT')
    
    Returns:
        str: Validated and uppercase symbol
    
    Raises:
        ValueError: If symbol format is invalid
    """
    symbol = symbol.upper()
    if not symbol.endswith('USDT'):
        raise ValueError("Only USDT pairs supported (e.g., BTCUSDT, ETHUSDT)")
    if len(symbol) < 5:
        raise ValueError("Invalid symbol format")
    return symbol


def validate_side(side: str) -> str:
    """
    Validate order side.
    
    Args:
        side: Order side ('BUY' or 'SELL')
    
    Returns:
        str: Validated and uppercase side
    
    Raises:
        ValueError: If side is not BUY or SELL
    """
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side.upper()


def validate_order_type(order_type: str) -> str:
    """
    Validate order type.
    
    Args:
        order_type: Order type ('MARKET' or 'LIMIT')
    
    Returns:
        str: Validated and uppercase order type
    
    Raises:
        ValueError: If order type is not MARKET or LIMIT
    """
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type.upper()


def validate_quantity(qty: str) -> float:
    """
    Validate order quantity.
    
    Args:
        qty: Order quantity as string
    
    Returns:
        float: Validated quantity
    
    Raises:
        ValueError: If quantity is not positive or not a valid number
    """
    try:
        qty = float(qty)
    except ValueError:
        raise ValueError("Quantity must be a valid number")
    
    if qty <= 0:
        raise ValueError("Quantity must be positive")
    return qty


def validate_price(price: str) -> float:
    """
    Validate order price.
    
    Args:
        price: Order price as string
    
    Returns:
        float: Validated price
    
    Raises:
        ValueError: If price is not positive or not a valid number
    """
    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a valid number")
    
    if price <= 0:
        raise ValueError("Price must be positive")
    return price
