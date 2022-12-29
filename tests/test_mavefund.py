import os

import pytest

from mavefund import Client, error
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("TEST_TOKEN")


def test_client_works():
    client = Client(KEY)
    df = client("AAPL")
    print(df)
    assert df is not None


# def test_bad_api_key_raises_error():
#     with pytest.raises(error.InvalidAPIKeyException):
#         client = Client("invalid")


def test_client_context_manager():
    with Client(KEY) as client:
        df = client("AAPL")
        assert df is not None


# def test_client_context_manager_fails():
#     with pytest.raises(error.InvalidAPIKeyException):
#         with Client("invalid") as client:
#             df = client("AAPL")


def test_invalid_ticker():
    client = Client(KEY)
    with pytest.raises(error.InvalidTickerException):
        df = client("invalid")


# def test_not_found_symbol():
#     client = Client(KEY)
#     with pytest.raises(error.TickerNotFoundException):
#         df = client("LMAO")
