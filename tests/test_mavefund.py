import os
from mavefund import Client
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("TEST_KEY")


def test_client_works():
    client = Client(KEY)
    df = client("AAPL")
    print(df)
    assert df is not None
