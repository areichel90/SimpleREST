from flask import Flask
app = Flask(__name__)

@app.route('/success/<name>')
def test():
    return "This Works"

if __name__ == "__main__":
    app.run(debug=True)