from flask import Flask, jsonify

app = Flask(__name__)

people = [
  {
    "id": 0,
    "name": "Mario",
    "surname": "Rossi"
  },
  {
    "id": 1,
    "name": "Giovanni",
    "surname": "Verdi"
  },
  {
    "id": 2,
    "name": "Paolo",
    "surname": "Galli"
  }
]


@app.route('/', methods=['GET'])
def firstpage():
    return "This is the first page"


@app.route('/<name>', methods=['GET'])
def hi(name):
    return "Hi %s" % name


@app.route('/getall', methods=['GET'])
def getall():
    return jsonify(people)






if __name__ == "__main__":
    app.run(debug=True)
