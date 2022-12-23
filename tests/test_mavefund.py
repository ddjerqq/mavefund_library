import os
from mavefund import Client


KEY = os.getenv("TEST_KEY")


def test_it_works():
    client = Client(KEY)
    df = client("AAPL")
    print(df)
    client.close()
