import subprocess
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def parse_data():
    sents = request.json['sents']
    in_filename = "input.txt"
    out_filename = "output.txt"
    with open(in_filename, 'w') as f:
        for sent in sents:
            f.write(sent)
            f.write('\n')

    cmds = ["python", "python/ner/extractEntities.py",
            in_filename, "-o", out_filename]
    subprocess.call(cmds)

    with open(out_filename, 'r') as f:
        lines = f.readlines()
    return jsonify({"parsed": lines})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
