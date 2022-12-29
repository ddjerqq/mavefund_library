from __future__ import annotations

import re

import pandas as pd
import requests
import logging
import warnings

from .symbol import Symbol, SymbolDto
from . import error


__all__ = (
    "Client"
)

warnings.filterwarnings("ignore")
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
        self.__base_url = "https://mavefund.com"

        self.__session = requests.Session()
        self.__session.cookies.set("token", self.__api_key)


    def __call__(
            self,
            ticker: str,
    ) -> pd.DataFrame:
        """Get records for a given company as a pandas DataFrame.

        :param ticker: The stock ticker symbol for the company.
        :return: A pandas DataFrame.
        """
        symbol_regex = r"^[a-zA-Z]{1,5}$"

        if not re.match(symbol_regex, ticker):
            raise error.InvalidTickerException(ticker)

        symbol = ticker.upper()
        url = f"{self.__base_url}/api/v1/records/get/{symbol}"

        try:
            resp = self.__session.get(url, verify=False)
            resp.raise_for_status()

        except requests.exceptions.Timeout:
            logger.error(
                "request timeout, please check your internet connection,"
                "or the server status at https://mavefund.com please try again in 5 minutes or report this bug to us!"
            )

        except requests.exceptions.ConnectionError:
            logger.error(
                "connection error, servers may be down. please try again in 5 minutes or report this bug to us!"
            )

        except requests.exceptions.HTTPError as e:
            response: requests.Response = e.response
            if response.status_code == 404:
                raise error.TickerNotFoundException(symbol)
            elif response.status_code == 401:
                raise error.UnauthorizedException()
            elif response.status_code == 403:
                raise error.ForbiddenException()
            else:
                logger.exception(
                    "HTTPError occurred while trying to fetch data. "
                    "please report this to us! \n"
                    f"{e}",
                    stack_info=True
                )

        except Exception as e:
            logger.exception(
                "exception occurred while trying to fetch data. please report this to us!\n"
                f"{e}",
                stack_info=True
            )

        else:
            symbol = resp.json()
            symbol_dto = SymbolDto(**symbol)
            symbol = symbol_dto.to_symbol()

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
