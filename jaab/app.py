from flask import Flask

from jaab.lib.route import set_routes

jaab_app = Flask(__name__)


def run_app():
    jaab_app.config['DEBUG'] = True
    set_routes(jaab_app)
    jaab_app.run()

if __name__ == "__main__":
    run_app()
