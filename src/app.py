#!/usr/bin/env python3
#!/Users/stevevanschouwen/my_flask_app/venv/bin/
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
<h2> Please input text string then click Submit button</h2>
     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text


@app.route("/svs", methods=["GET"])
def svs():
   return "HELLO"


def wutt():
   return "WUTT"

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)



    return app
