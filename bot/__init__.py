"""
Binance Futures Trading Bot

A modular trading bot for placing orders on Binance Futures testnet.

Modules:
    client: Binance API client wrapper
    orders: Order placement logic with notional validation
    validators: Input validation functions
    logging_config: Logging configuration
"""

__version__ = "1.0.0"
__author__ = "Trading Bot Team"

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.logging_config import setup_logging

__all__ = [
    "BinanceFuturesClient",
    "place_order",
    "setup_logging",
]
