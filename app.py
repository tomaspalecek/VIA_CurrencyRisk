from flask import Flask, render_template, request
from stock_data import stock_data,currency_data,stock_data_foreign,stock_data_currency_risk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    from_cur = request.form['from']
    to_cur = request.form['to']
    stock = request.form['stock']



    if request.form.get('exchange_b')=='Exchange Rate':
        labels,values = currency_data(from_cur,to_cur)
        return render_template('index.html', title='Exchange rates ' + from_cur +"/" + to_cur, labels=labels, values=values)
    if request.form.get('stock_b') == "Stock Price":
        labels, values = stock_data(stock)
        return render_template('index.html', title=stock + '(USD)', labels=labels, values=values)
    if request.form.get('stock_foreign_b') == "Stock in Foreign Currency":
        labels, values = stock_data_foreign(stock,to_cur)
        return render_template('index.html', title=stock + '('+to_cur+')', labels=labels, values=values)
    if request.form.get('stock_currency_b') == "Stock Currency Risk":
        labels, values, values2 = stock_data_currency_risk(stock, to_cur)
        return render_template('index.html', title=stock + ' Currency Risk(USD/' + to_cur + ')', labels=labels, values=values, values2=values2)











if __name__ == '__main__':
    app.run(debug=True)