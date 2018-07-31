import matplotlib.pyplot as plt
from catalyst.api import order, record, symbol


def initialize(context):
    context.asset = symbol('btc_usd')


def handle_data(context, data):
    order(context.asset, 1)
    record(btc = data.current(context.asset, 'price'))

def analyze(context, perf):
    ax1 = plt.subplot(211)
    perf.portfolio_value.plot(ax=ax1)
    ax1.set_ylabel('portfolio value')
    ax2 = plt.subplot(212, sharex=ax1)
    perf.btc.plot(ax=ax2)
    ax2.set_ylabel('bitcoin price')
    plt.show()
