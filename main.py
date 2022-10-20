from configuration import rti_configuration
from flask_app import flask_wsgi_app

flask_wsgi_app.start_server(rti_configuration.options)
