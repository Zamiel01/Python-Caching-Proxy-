# Python Caching Proxy

A simple Python-based caching proxy server that forwards HTTP requests to a target server and caches responses for faster repeated access. Built using `http.server`, `socketserver`, and `requests`.

---

project url: https://roadmap.sh/projects/caching-server

## Features

- Forwards **GET requests** to a target server.
- Caches responses in memory to reduce repeated network calls.
- Handles **POST requests** (currently returns a simple acknowledgment).
- Minimal and easy-to-understand Python implementation.
- Customizable server port and target server URL via CLI arguments.

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/python-caching-proxy.git
cd python-caching-proxy
Install dependencies:

bash
Copy code
pip install requests
Usage
Run the proxy server using Python:

bash
Copy code
python proxy_server.py --port 8000 --url http://example.com
Arguments
Argument	Description
--port	Port on which the proxy server will run (default: 8000)
--url	The base URL of the server to which requests will be forwarded

Example
Forward requests to http://example.com on port 9000:

bash
Copy code
python proxy_server.py --port 9000 --url http://example.com
How It Works
The browser (or client) sends a GET or POST request to the proxy server.

GET requests:

If the requested URL is already in cache, the server responds with cached content.

If not, the server fetches the content from the target URL, stores it in cache, and returns it to the client.

POST requests:

Currently, the server prints the POST body and returns a simple acknowledgment.

Example Output
GET request:

pgsql
Copy code
Incoming GET request → /path
Fetching from target server
Subsequent GET request to the same path:

pgsql
Copy code
Incoming GET request → /path
Serving from cache
POST request:

bash
Copy code
Incoming POST request → /submit
POST body: b'name=John&age=25'
Dependencies
Python 3.6+

requests library

Install dependencies with:

bash
Copy code
pip install requests
License
This project is licensed under the MIT License. See LICENSE for details.

Author
NKUIN EUGENE MBENG – Zamiel01
