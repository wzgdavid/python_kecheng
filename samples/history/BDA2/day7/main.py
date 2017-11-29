from flask import Flask, render_template
from read_data import read_pokemon
app = Flask(__name__)

@app.route('/')
def hello_world():

    return 'Hello World!'

@app.route('/hello/')
def hello():
    names = ['tom', 'cat', 'jeryy']
    names2 = {'tom':222, 'cat':2223}
    df = read_pokemon()
    return render_template('hello.html', usernames=names, names2=names2, df=df)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')