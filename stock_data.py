import requests

API_KEY = '3VN6MMFYXUT6XSNZ'
API_KEY_OPEN_RATES = '74a967c65c5c4595acd9c3fd66ed39a4'

def stock_data(stock_symbol):
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+stock_symbol+'&apikey=' + API_KEY)
    data = {}
    if (r.status_code == 200):
      data = r.json()["Time Series (Daily)"]

    labels = []
    values = []



    for label,value in data.items():
        labels.append(label)
        values.append(value['1. open'])

    labels = list(reversed(labels))
    values = list(reversed(values))

    return labels,values

def stock_data_foreign(stock_symbol,to_symbol):
    stock_labels,stock_values = stock_data(stock_symbol)
    currency_labels,currency_values = currency_data('USD',to_symbol)

    risk_values = [float(a) * float(b) for a, b in zip(stock_values, currency_values)]
    risk_values = map(str,risk_values)
    return stock_labels,risk_values


def stock_data_currency_risk(stock_symbol, to_symbol):
    # Setrime api
    stock_labels, stock_values = stock_data(stock_symbol)
    currency_labels, currency_values = currency_data('USD', to_symbol)

    risk_values = [float(a) * float(b) for a, b in zip(stock_values, currency_values)]
    risk_values = map(str, risk_values)

    current_rate = float(currency_values[-1])
    # current_rate = 10

    current_values = [current_rate*float(a) for a in stock_values]
    current_values = map(str,current_values)


    return stock_labels, risk_values, current_values


def currency_data(from_symbol,to_symbol):
    r = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol='+from_symbol+'&to_symbol='+to_symbol+'&apikey=' + API_KEY)
    # r = requests.get('https://openexchangerates.org/api/latest.json?app_id=' + API_KEY_OPEN_RATES)
    data = {}
    if (r.status_code == 200):
        data = r.json()['Time Series FX (Daily)']

    labels = []
    values = []

    for label,value in data.items():
        labels.append(label)
        values.append(value['1. open'])

    labels = list(reversed(labels))
    values = list(reversed(values))

    return labels,values


if __name__=="__main__":
    print(currency_data('EUR','CZK')[1])

