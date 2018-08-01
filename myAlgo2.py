import pytz
import numpy as np
from pyswarm import pso
import matplotlib.pyplot as plt
from datetime import datetime

from catalyst.api import record, order, symbol
from catalyst.utils.run_algo import run_algorithm

def initialize(context):
    context.asset = symbol('btc_xrp')
    persistence = []

def handle_data(context, data):

    lastPrice = data.history(context.asset, 'price', bar_count = 3, frequency = '1D')
    lastVol = data.history(context.asset, 'volume', bar_count = 3, frequency = '1D')
    dum = [1,2,3]
    
    



    record(btc = data.current(context.asset, 'price'))



def analyze(context, results):
    # Form DataFrame with selected data
    plt.plot(results.portfolio_value)
    plt.show()
    print("showing plot")


if __name__ == '__main__':
    # Bitcoin data is available from 2015-3-2. Dates vary for other tokens.
    start = datetime(2018, 5, 22, 0, 0, 0, 0, pytz.utc)
    end = datetime(2018, 7, 29, 0, 0, 0, 0, pytz.utc)
    results = run_algorithm(initialize=initialize,
                            handle_data=handle_data,
                            analyze=analyze,
                            start=start,
                            end=end,
                            exchange_name='bittrex',
                            capital_base=100000,
                            quote_currency='btc')

