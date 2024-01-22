from flask import Flask, render_template, make_response


class MaintenanceModeMiddleware:
    def __init__(self, wsgi_call_back, app, maintenance_mode=False):
        self.wsgi_call_back = wsgi_call_back
        self.app = app
        self.maintenance_mode = maintenance_mode

    def __call__(self, environ, start_response):
        if self.maintenance_mode:
            with self.app.app_context():
                response = make_response(render_template('home/maintenance.html'), 503)
            return response(environ, start_response)
        return self.wsgi_call_back(environ, start_response)
