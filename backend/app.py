import json
from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route('/api/urls', methods=['GET', 'POST'])
def urls():
    if request.method == 'GET':
        with open('urls.json', 'r') as fp:
            db = json.load(fp)
            return json.dumps(db)
    elif request.method == 'POST':
        with open('urls.json', 'r') as fp:
            db = json.load(fp)
        j = request.form.get('url')
        if not j:
            return 'URL missing in json', 400
        with open('urls.json', 'w') as fp:
            db.append(j)
            db = list(set(db))
            json.dump(db, fp)
        return "Success"

app.run(host='0.0.0.0')
