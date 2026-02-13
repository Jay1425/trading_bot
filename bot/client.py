from binance.client import Client
from typing import Dict, Any


class BinanceFuturesClient:
    """
    Wrapper for Binance Futures API client configured for testnet.
    
    This client is pre-configured to connect to Binance Futures testnet
    at https://testnet.binancefuture.com for safe testing without real funds.
    
    Attributes:
        client: Binance API client instance
    """
    
    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize Binance Futures client with testnet configuration.
        
        Args:
            api_key: Binance testnet API key
            api_secret: Binance testnet API secret
        """
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    
    def create_order(self, **kwargs) -> Dict[str, Any]:
        """
        Create a futures order on Binance testnet.
        
        Args:
            **kwargs: Order parameters (symbol, side, type, quantity, etc.)
        
        Returns:
            dict: Order response from Binance API
        
        Raises:
            Exception: If API request fails
        """
        return self.client.futures_create_order(**kwargs)
