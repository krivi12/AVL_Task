import flask
from flask import request
import hashlib

app = flask.Flask(__name__)


@app.route('/get-hash', methods=['POST'])
def getHash():
    json = request.json
    if not "rawValue" in json:
        return "Please specify rawValue", 400

    hash_func = json.get("hashFunc")
    if hash_func is None:
        hash_func = "sha256"

    h = hashlib.new(hash_func)
    h.update(str.encode(json["rawValue"]))
    return h.hexdigest()


app.run()
