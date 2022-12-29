# MaveFund API Client Library 0.0.8

<img alt="logo" height="120" src="mavefund.jpg" title="mavefund logo" />

The official library for [mavefund](https://mavefund.com) used to download data from
the API as pandas dataframes for easy accessibility.

created and maintained by [ddjerqq](https://github.com/ddjerqq)

## Installation

Run this in your terminal:
```bash
pip install mavefund
```

## Getting started

* To use the library you need to acquire an API key from [the official website](https://mavefund.com)
* After that import the library into your python code

```python
import mavefund as mf
with mf.Client(api_key="YOUR KEY") as client:
    apple_df = client("AAPL")
# access the dataframe here
```

## Documentation

### [Client](https://github.com/ddjerqq/mavefund_library/blob/master/mavefund/client.py)
#### creation:
There are two ways to create a client, a context manager and a regular object.

```python
from mavefund import Client

# context manager (recommended)
with Client(api_key="KEY") as client:
    apple_df = client("AAPL")

    
# regular object
client = Client("KEY")
df = client("AAPL")
client.close()
```
