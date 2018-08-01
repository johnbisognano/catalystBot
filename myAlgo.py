import pytz
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from catalyst.api import record, order, symbol, cancel_order, get_open_orders
from catalyst.utils.run_algo import run_algorithm

def initialize(context):
    context.asset = symbol('btc_usdt')
    context.is_buying = True

def handle_data(context, data):
    last3 = []

    last3orig = data.history(context.asset, 'price', bar_count = 3, frequency = '1T')
    last3[:] = last3orig




    if context.portfolio.positions[context.asset].amount == 0:
        if sorted(last3) == last3:
            print("here")
            cash = context.portfolio.cash
            context.cur_price = data.current(context.asset, 'price')
            buy_amount = int(min(cash // context.cur_price, 100000 // context.cur_price))
            order(context.asset, buy_amount)

    else:
        if data.current(context.asset, 'price') < .9 * context.cur_price:
            num = context.portfolio.positions[context.asset].amount
            order(context.asset, -num)

        if  sorted(last3) != last3 and (context.cur_price * 1.15) < data.current(context.asset, 'price'):
            print("HERE")
            num = context.portfolio.positions[context.asset].amount
            order(context.asset, -num)



    record(btc = data.current(context.asset, 'price'))



def analyze(context, results):
    # Form DataFrame with selected data
    plt.plot(results.portfolio_value)
    plt.show()
    print("showing plot")


if __name__ == '__main__':
    # Bitcoin data is available from 2015-3-2. Dates vary for other tokens.
    start = datetime(2018, 1, 22, 0, 0, 0, 0, pytz.utc)
    end = datetime(2018, 7, 29, 0, 0, 0, 0, pytz.utc)
    results = run_algorithm(initialize=initialize,
                            handle_data=handle_data,
                            data_frequency='minute',
                            analyze=analyze,
                            start=start,
                            end=end,
                            exchange_name='poloniex',
                            capital_base=100000,
                            quote_currency='usdt')

