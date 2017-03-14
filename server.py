from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from firebase import firebase
import SocketServer

firebase = firebase.FirebaseApplication('https://ais-accounting.firebaseio.com/', None)
new_user = 'Name:Peng'



class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        #self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
    	global firebase
        content_length = int(self.headers.getheader('content-length', 0))
        post_data = self.rfile.read(content_length)
        print post_data
        result = firebase.post('/ais-accounting/users', post_data)
        print result
        #self._set_headers()
        #self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()