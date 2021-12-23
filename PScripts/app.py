from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def detect():
    data = request.get_json(force=True)["text"]
    sentence = Sentence(data,use_tokenizer=scp)
    tagger.predict(sentence)
    r = []
    for i, e in enumerate(sentence.get_spans()):
      r.append({
          "ind" : i,
          "token" : e.text,
          "value" : e.tag,
          "score" : e.score 
      })
    return jsonify(r), 200

if __name__ == '__main__':
    app.run()
