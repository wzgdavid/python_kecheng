from flask import Flask,render_template
from functions import get_page, record_clicked, recommend
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/list_housing/<int:n>")
def list_housing(n):
    rows = get_page(n)
    recommended = recommend()
    return render_template(r'list.html', rows=rows, recommended=recommended)

@app.route("/record_click/<int:idx>")
def record_click(idx):
    record_clicked(idx)
    return ''

if __name__ == '__main__':
    app.run(debug=True)