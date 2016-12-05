from flask import Flask

from jaab.lib.route import set_routes


def run_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    set_routes(app)
    app.run()

if __name__ == "__main__":
    run_app()
