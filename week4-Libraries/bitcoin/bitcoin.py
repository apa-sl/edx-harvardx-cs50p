# CS50p Problem Set 4: Bitcoin Price Index
# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
#
# Goal: user input number of bitcoins (float) and is informed about their current value (CoinDesk price)
# Author: Adam Labedzki 2023-01-13

import sys
import requests

"""
pseudocode:
1. verify number of bitcoins provided as cmd line parameter and that it is a float number
2. get current btc price from API
3. calculate and print price of provided sum of bitcoins
"""


def main():
    # custom deffined error for no cmd-line args
    class ParametersError(Exception):
        "Raised when user will not provide any command-line params"
        pass

    # check if there is 1 param in the cmd-line
    try:
        if len(sys.argv) == 2:
            # check if it is a float
            if not isfloat(sys.argv[1]):
                raise ValueError
        else:
            raise ParametersError
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except ParametersError:
        sys.exit("Missing command-line argument")
    else:
        # store provided btc quantity in a variable
        btc_quantity = float(sys.argv[1])

    # try to download BTC price
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        print("RequestException")
    except requests.ConnectionError:
        print("Connection Error")
    except requests.HTTPError:
        print("HTTP Error")
    except requests.URLRequired:
        print("URL is requrired")
    except requests.Timeout:
        print("The request timed out")
    else:
        # calculate value of all bitcoins & print
        btc_price_usd = r.json()["bpi"]["USD"]["rate_float"]
        btc_total_usd = btc_quantity * btc_price_usd
        print(f"${btc_total_usd:,.4f}")


# check if provided number is a float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()