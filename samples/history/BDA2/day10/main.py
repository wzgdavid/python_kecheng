from flask import Flask, render_template
from logic import get_page, record_index
from anjuke2 import recommend
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<int:n>')
def hello(n):
    rows = get_page(n)
    recommends = recommend()
    return render_template('hello.html', rows=rows,recommends=recommends)

@app.route('/record_click/<int:idx>')
def record_click(idx):
    record_index(idx)
    return ''

if __name__ == '__main__':
    app.run(debug=True)