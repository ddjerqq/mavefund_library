class TickerNotFoundException(Exception):
    def __init__(self, ticker):
        self.ticker = ticker

    def __str__(self):
        return f"ticker not found: {self.ticker}"



class InvalidAPIKeyException(Exception):
    def __str__(self):
        return f"invalid API_KEY"



class InvalidTickerException(Exception):
    def __init__(self, ticker):
        self.ticker = ticker

    def __str__(self):
        return f"invalid ticker: {self.ticker}"



class UnauthorizedException(Exception):
    def __str__(self):
        return "unauthorized, is the API_KEY valid?"



class ForbiddenException(Exception):
    def __str__(self) -> str:
        return "forbidden, please check your API_KEY and try again. are you supposed to have access to this resource?"
