from flask import Flask, render_template, jsonify

app = Flask(__name__)

WEARS = [
  {
    'id': 1,
    'title': 'Bimbo Gown',
    'Category': 'Office wear',
    'Price': 'Naira. 20,000'
  },
  {
    'id': 2,
    'title': 'Eno Gown',
    'Category': 'Children wear',
    'Price': 'Naira. 15,000'
  },
  {
    'id': 3,
    'title': 'Two piece',
    'Category': 'Casual wear'
  },
  {
    'id': 4,
    'title': 'Emeka piece',
    'Category': 'Men Wear',
    'Price': '#25,000'
  }
]

@app.route("/")
def hello_HOJ():
    return render_template('home.html', 
                           wears=WEARS, 
                           company_name='House of Jele')

@app.route("/api/wears")
def list_wears():
  return jsonify(WEARS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
