import logging
import os


def setup_logging() -> None:
    """
    Configure logging for the trading bot.
    
    Creates a 'logs' directory if it doesn't exist and sets up
    file-based logging with INFO level. Logs include timestamp,
    log level, module name, and message.
    
    Log file location: logs/trading.log
    """
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/trading.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
