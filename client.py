################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URL
QUERY = "http://localhost:8080/query?id={}"

# Number of server requests
N = 500


def getDataPoint(quote):
    """
    Produce all the needed values to generate a datapoint.

    Parameters:
    quote (dict): Dictionary containing the quote information.

    Returns:
    tuple: Tuple of stock name, bid price, ask price, and average price.
    """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """
    Get ratio of price_a and price_b.

    Parameters:
    price_a (float): First price to be used in the ratio calculation.
    price_b (float): Second price to be used in the ratio calculation.

    Returns:
    float or None: The ratio of price_a and price_b, or None if price_b is 0.
    """
    if price_b == 0:
        return None
    return price_a / price_b


# Main
if __name__ == "__main__":

    # Query the price once every N seconds.
    # Get a price directory where the key-value pair is stock name-price
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(
            QUERY.format(random.random())).read())

        prices = {}
        """ ----------- Update to get the ratio --------------- """
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" %
                  (stock, bid_price, ask_price, price))

        print("Ratio %s" % (getRatio(prices['ABC'], prices['DEF'])))
