from __future__ import annotations

import pandas as pd
import requests
import logging


__all__ = (
    "Client"
)

from . import Symbol

logger = logging.getLogger("mavefund")


class Client:
    """MaveFund API Client
    """
    def __init__(
            self,
            api_key: str,
    ) -> None:
        """Create a new instance of the API client.

        :param api_key: The API key to use for authentication. get yours at https://mavefund.com
        """
        self.__api_key = api_key
        self.__base_url = "https://api.mavefund.com"

        self.__session = requests.Session()
        self.__session.cookies.set("token", self.__api_key)


    def __call__(
            self,
            symbol: str,
    ) -> pd.DataFrame:
        """Get records for a given company as a pandas DataFrame.

        :param symbol: The stock ticker symbol for the company.
        :return: A pandas DataFrame.
        """
        url = f"{self.__base_url}/api/v1/records/get?ticker={symbol}"

        try:
            resp = self.__session.get(url)
        except requests.exceptions.Timeout:
            logger.error("request timeout, please try again in 5 minutes or report this bug to us!")
        except requests.exceptions.ConnectionError:
            logger.error("connection error, please try again in 5 minutes or report this bug to us!")
        except Exception as e:
            logger.exception(
                "exception occurred while trying to fetch data. please report this to us!\n"
                f"{e}",
                stack_info=True
            )
        else:
            resp.raise_for_status()

            symbol = resp.json()
            symbol = Symbol(**symbol)

            return symbol.df

    def close(self) -> None:
        """Close the API client.

        alternatively use the context manager:
            >>> with Client(api_key="YOUR_API_KEY") as client:
            >>>     records = client("AAPL")
        """
        self.__session.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, exc_type: Exception, exc_val: ..., exc_tb: ...) -> None:
        self.close()
