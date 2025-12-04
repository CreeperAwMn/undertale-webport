from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the server address and port
HOST = 'localhost'  # Or '0.0.0.0' to listen on all available interfaces
PORT = 8000

# Create an HTTP server instance
httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Serving HTTP on {HOST} port {PORT} (http://{HOST}:{PORT}/)")

# Start the server and keep it running
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    httpd.server_close()