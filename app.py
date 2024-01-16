from crypt import methods
from flask import Flask

app = Flask (__name__)

@app. route('/', methods = ['GET', 'POST'])
def main():
    return "Ryan AGZ"


# @app. route('/', methods = ['GET', 'POST'])
# def main():
#     return "Bienvenue"


if __name__ == '__main__':
    app.run("0.0.0.0" , port = 80)