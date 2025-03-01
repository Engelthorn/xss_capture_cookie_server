#!/usr/bin/python3.12
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie
from urllib.parse import urlparse
from ssl import wrap_socket


class RequestHandler(BaseHTTPRequestHandler):

    def do_get_request(self):
        params = urlparse(self.path).query
        print(params)


if __name__ == '__main__':
    port = 443
    server = HTTPServer(('localhost', port), RequestHandler)
    print('Starting Server')
    server.socket = wrap_socket(server.socket, certfile='server.crt', keyfile='server.key', server_side=True)
    server.serve_forever()
