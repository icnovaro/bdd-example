from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/colors")
def colors():
    colors = {
        "primary": ["yellow", "blue", "red"],
        "secondary": ["green", "violet", "orange"],
        "tertiary": ["orange-yellow", "red-orange"]
        }
    
    kind = request.args.get('kind')
    
    return { "colors": colors.get(kind) }, 200
