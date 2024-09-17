from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/callback', methods=["GET", "POST"])
def redirect():
    tok = request.args.get("code")
    print(tok)
    with open("token.bin", "w+") as tokf:
        tokf.write(tok)
        tokf.flush()
        tokf.close()
    return "OK"


app.run(host="localhost", port=8879, debug=True)
