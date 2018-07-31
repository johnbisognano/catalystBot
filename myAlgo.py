import pytz
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from catalyst.api import record, order, symbol
from catalyst.utils.run_algo import run_algorithm


def initialize(context):
    context.asset = symbol('btc_usdt')


def handle_data(context, data):
    last3 = data.history(context.asset, 'price', bar_count = 3, frequency = '1T')
    print(last3[0])
    order(context.asset, 1)
    record(btc = data.current(context.asset, 'price'))



def analyze(context, results):
    # Form DataFrame with selected data
    plt.plot(results.portfolio_value)
    plt.show()
    pint("showing plot")


if __name__ == '__main__':
    # Bitcoin data is available from 2015-3-2. Dates vary for other tokens.
    start = datetime(2018, 5, 1, 0, 0, 0, 0, pytz.utc)
    end = datetime(2018, 7, 30, 0, 0, 0, 0, pytz.utc)
    results = run_algorithm(initialize=initialize,
                            handle_data=handle_data,
                            analyze=analyze,
                            data_frequency='minute',
                            start=start,
                            end=end,
                            exchange_name='poloniex',
                            capital_base=100000,
                            quote_currency='usdt')