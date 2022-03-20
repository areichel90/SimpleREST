from flask import Flask, redirect, url_for, request, jsonify
import datetime

app = Flask(__name__)

# this is to be replaced with a schema that all clients will
# use to share payloads back and forth between the server
test_payload = [
    {"id": "test_payload_1",
    "author": "macbook_pro",
    "payload": "testing, testing"}
]

@app.route("/sandbox", methods=['GET','POST'])
def sandbox():
    print("Request: ", request)

    ''' GET Method '''
    if request.method == "GET":
        return jsonify(test_payload)
    else:
        'Nothing Found', 404

    ''' PUT/POST Method '''
    if (request.method == "POST" or request.method == "PUT"):
        new_id = request.form["id"]
        new_author = request.form["author"]
        new_payload = request.form["payload"]

        if request.method == "POST":
            new_entry = {
                "id":new_id,
                "author":new_author,
                "payload":new_payload
            }
            test_payload.append(new_entry)
            return jsonify(test_payload)


@app.route('/sandbox/<string:id>', methods=['GET','PUT','POST'])
def single_entry(id):
    print("Request: ", request, "ID: ", id)

    ''' GET Method '''
    if request.method == "GET":
        for entry in test_payload:
            if entry["id"] == id:
                return jsonify(entry)
    else:
        'Nothing Found', 404

    ''' PUT/POST Method '''
    if (request.method == "POST" or request.method == "PUT"):
        new_id = request.form["id"]
        new_author = request.form["author"]
        new_payload = request.form["payload"]

        if request.method == "POST":
            new_entry = {
                "id":new_id,
                "author":new_author,
                "payload":new_payload
            }
            test_payload.append(new_entry)
            return jsonify(test_payload)

        elif request.method == "PUT":
            for entry in test_payload:
                if entry["id"] == id:
                    entry["id"] = new_id
                    entry["author"] = new_author
                    entry["title"] = new_payload
                    updated_entry = {
                        "id":entry["id"],
                        "author":entry["author"],
                        "title":entry["title"] 
                    }
            return jsonify(entry)



@app.route('/') 
def home():
    return "This Works!"

@app.route("/<name>")
def print_name(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", 
            port=8000,
            debug=True)