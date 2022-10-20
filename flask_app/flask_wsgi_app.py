from flask import Flask
from cheq_rti_wsgi_middleware.RtiWsgiMiddleware import RtiMiddleware


def start_server(options):
    app = Flask(__name__)

    rti_options = options.copy()
    rti_options.update({'app': app.wsgi_app})

    app.wsgi_app = RtiMiddleware(rti_options)

    @app.route("/")
    def index():
        return "Hello world"

    app.run('0.0.0.0', 8080)
