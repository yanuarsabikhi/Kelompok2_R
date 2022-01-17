from flask import Flask, render_template

application = Flask(__name__)
@application.route('/')
def index():
    return render_template('index.html')

@application.route('/fibonacci')
def fibo():
    return render_template('fibonacci.html')

@application.route('/faktorial')
def faktorial():
    return render_template('faktorial.html')

@application.route('/ganjilgenap')
def ganjilgenap():
    return render_template('ganjilgenap.html')

if __name__ == '__main__':
    application.run(debug=True)
