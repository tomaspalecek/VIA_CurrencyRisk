from flask import Flask, render_template, request, jsonify
from stock_data import stock_data,currency_data,stock_data_foreign,stock_data_currency_risk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',legend="")

@app.route('/', methods=['POST'])
def my_form_post():
    from_cur = request.form['from']
    to_cur = request.form['to']
    stock = request.form['stock']



    if request.form.get('exchange_b')=='Exchange Rate':
        labels,values = currency_data(from_cur,to_cur)
        return render_template('index.html', title='Exchange rates ' + from_cur +"/" + to_cur, labels=labels, values=values,legend="")
    if request.form.get('stock_b') == "Stock Price":
        labels, values = stock_data(stock)
        return render_template('index.html', title=stock + '(USD)', labels=labels, values=values,legend="")
    if request.form.get('stock_foreign_b') == "Stock in Foreign Currency":
        labels, values = stock_data_foreign(stock,to_cur)
        return render_template('index.html', title=stock + '('+to_cur+')', labels=labels, values=values,legend="")
    if request.form.get('stock_currency_b') == "Stock Currency Risk":
        labels, values, values2 = stock_data_currency_risk(stock, to_cur)
        return render_template('index.html', title=stock + ' Currency Risk(USD/' + to_cur + ')', labels=labels, values=values, values2=values2, legend=["Continous exchange rate","Current exchange rate"])

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cur',methods=['GET'])
def cur_all():
    from_cur = request.args.get('from')
    to_cur = request.args.get('to')
    data = currency_data(from_cur,to_cur)
    dict_data = {'dates':data[0],'values':data[1]}
    return jsonify(dict_data)

@app.route('/cur/today',methods=['GET'])
def cur_today():
    from_cur = request.args.get('from')
    to_cur = request.args.get('to')
    data=currency_data(from_cur,to_cur)[1][-1]
    dict_data = {'value':data}
    return jsonify(dict_data)


@app.route('/stock',methods=['GET'])
def stock_all():
    stock_name = request.args.get('symbol')
    data = stock_data(stock_name)
    dict_data = dict_data = {'dates':data[0],'values':data[1]}
    return jsonify(dict_data)

@app.route('/stock/cur',methods=['GET'])
def stock_cur():
    stock_name = request.args.get('symbol')
    stock_cur = request.args.get('cur')
    data = stock_data_foreign(stock_name,stock_cur)
    dict_data = {'dates': data[0], 'values': data[1]}
    return jsonify(dict_data)

@app.route('/stock/risk',methods=['GET'])
def stock_risk():
    stock_name = request.args.get('symbol')
    stock_cur = request.args.get('cur')
    data = stock_data_currency_risk(stock_name,stock_cur)
    dict_data = {'dates': data[0], 'values_cont': data[1],'values_cur': data[2]}
    return jsonify(dict_data)




# @app.route('/stockcurrency/<stock_name>/<currency>/all', methods=['GET'])
# def stock_currency(stock_name,currency):
#     return jsonify(stock_data_foreign(stock_name,currency))
#
# @app.route('/stockcurrency/<stock_name>/<currency>/today', methods=['GET'])
# def stock_currency_today(stock_name,currency):
#     return jsonify(stock_data_foreign(stock_name,currency)[1][-1])
#
# @app.route('/stockcurrencyrisk/<stock_name>/<currency>/all', methods=['GET'])
# def stock_currency_risk_all(stock_name,currency):
#
#     return jsonify(stock_data_currency_risk(stock_name, currency)[0:1])
#
#
#








if __name__ == '__main__':
    app.run(debug=True)