import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def webhook():
    user_name = request.form['user_name'] 
    text = request.form['text']

    if 'hello' in text:
        return_text = {'text': 'Hello %s' % args}
        return json.dumps(return_text)
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
