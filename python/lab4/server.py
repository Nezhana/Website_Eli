from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обробник з реалізованим методом do_GET."""

    def do_GET(self):
        self.send_response(200) #200 - код відповіді, що сторінка виявлена
        self.send_header("Content-type", "text/html") #http-заголовки, тип відповіді - html-розмітка
        self.end_headers()
        #вивід браузера (потоки сервера):
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простий HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>GET-запит був отриман.</body></html>'.encode())

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class) #сервер
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

def main():
    #http://127.0.0.1:8000/
    run(handler_class=HttpGetHandler)

if(__name__ == '__main__'):
    main()