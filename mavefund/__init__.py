"""MaveFund API Client

Examples:
    >>> from mavefund import Client

    >>> with Client(api_key="YOUR_API_KEY") as client:
    ...     records = client("AAPL")
"""

from .symbol import Symbol
from .client import Client

__all__ = (
    "Client",
    "Symbol",
)


__version__ = 0, 0, 1