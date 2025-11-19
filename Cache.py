import argparse
import http.server
import socketserver
import requests

# -------------------------------
# 1. Define a simple cache
# -------------------------------
cache = {}  # key: full_url, value: response content

# -------------------------------
# 2. Define a custom request handler
# -------------------------------
class CustomHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print(f"Incoming GET request → {self.path}")

        # Build full URL
        target_url = args.url
        full_url = target_url + self.path

        # Check if response is in cache
        if full_url in cache:
            print("Serving from cache")
            response_body = cache[full_url]
        else:
            print("Fetching from target server")
            try:
                response = requests.get(full_url)
                response_body = response.content
                cache[full_url] = response_body  # store in cache
            except requests.RequestException as e:
                self.send_response(502)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(f"Error forwarding request: {e}".encode())
                return

        # Send response to client
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(response_body)

# -------------------------------
# 3. Parse CLI arguments
# -------------------------------
parser = argparse.ArgumentParser(description="Python Caching Proxy CLI.")
parser.add_argument('--port', type=int, default=8000,
                    help="Port on which the caching proxy server will run")
parser.add_argument('--url', type=str, required=True,
                    help="URL of the server to which requests will be forwarded")
args = parser.parse_args()

# -------------------------------
# 4. Start server
# -------------------------------
PORT = args.port
print("Proxy server started")

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
