# The logic of the Flask application

import pandas as pd
from flask import Flask
from flask import jsonify
app = Flask(__name__)

# @app.route('/pandas')
# def pandas_sugar():
#     df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
#     return jsonify(df.to_dict())

@app.route('/')
def hello():
    """Return a friendly HTTP greeting"""
    print("I am inside Hello World")
    return 'Re kene!'

@app.route('/html/')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)