from werkzeug.serving import run_simple
# ...
from sylfk.wsgi_adapter import wsgi_app
from werkzeug.wrappers import Response

class SYLFk:

  # ?????
  def __init__(self):
    self.host = '127.0.0.1' # ????
    self.port = 8086  # ????
# ...
  # ????

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
