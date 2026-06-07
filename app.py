import http.server
import socketserver

# Tell Azure to serve files on port 8000 (standard for App Services)
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8000), handler) as httpd:
    httpd.serve_forever()
