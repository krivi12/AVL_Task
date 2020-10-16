import flask
from flask import request
import requests
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hash-html-page', methods=['POST'])
def getHtmlHash():

    url = request.json.get("url")
    if url is None:
        return "Please specify url", 400
    html_page = requests.get(url).text
    payload = {"rawValue": html_page}
    hashed_html_page = requests.post("http://localhost:5000/get-hash",
                                     data=json.dumps(payload), headers={"content-type": "application/json"}).text

    return hashed_html_page


app.run()
