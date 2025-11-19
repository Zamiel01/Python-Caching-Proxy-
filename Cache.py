import argparse
#http services
import http.server
import socketserver

#port through which server will run
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

parser = argparse.ArgumentParser(description="Python Caching Proxy CLI.")
parser.add_argument('--port', type=str, help="Enter the port on which the caching proxy server will run")
parser.add_argument('--url', type=int, help="Enter the URL of the server to which the requests will be forwarded.")
args = parser.parse_args()

