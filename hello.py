
from typing import Any
from flask import Flask
# from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/<string:name>")
def hello(name: str) -> Any:
    """_summary_

    Args:
        name (str): _description_

    Returns:
        str: _description_
    """
    return render_template('index.html', name=name)


@app.route("/")
def hello_world() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return "<h1>Hello, World!</h1>"
