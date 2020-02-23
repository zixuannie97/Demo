from werkzeug.serving import run_simple
import sylfk.exceptions as exceptions
# ...
from sylfk.wsgi_adapter import wsgi_app
from werkzeug.wrappers import Response
import os

class ExecFunc:
    def __init__(self, func, func_type, **options):
        self.func = func
        self.options = options
        self.func_type = func_type

class SYLFk:

  # ?????
  def __init__(self):
    self.host = '127.0.0.1' # ????
    self.port = 8086  # ????
    self.url_map = {}
    self.static_map = {}
    self.function_map = {}
    self.static_folder = static_folder
# ...
  # ????

  def add_url_rule(self, url, func, func_type, endpoint = None, **options):
     if endpoint is None:
          endpoint = func.__name__

     if url in self.url_map:
            raise exceptions.URLExistsError

     if endpoint in self.function_map and func_type != 'static':
         raise exceptions.EndpointExistsError

     self.url_map[url] = endpoint

     self.function_map[endpoint] = ExecFunc(func, func_type, **options)

  def dispatch_request(self, request):
      status = 200

      headers = {
              'Server': 'Niezixuan Framework'
            }

      return Response('<h1>Hello, Framework</h1>', content_type='text/html', headers = headers, status = status)

  def __call__(self, environ, start_response):
      return wsgi_app(self, environ, start_response)

  def run(self, host=None, port=None, **options):
    # ????????????????
    for key, value in options.items():
      if value is not None:
        self.__setattr__(key, value)

    # ?? host ?? None??? self.host
    if host:
        self.host = host

    # ?? port ?? None??? self.port
    if port:
        self.port = port

    # ??????????????????????? werkzeug ? run_simple
    run_simple(hostname=self.host, port=self.port, application=self, **options)
# ...
