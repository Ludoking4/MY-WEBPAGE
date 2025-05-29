import http.server
import socketserver
import webbrowser
import os

PORT = 8000
 
# Change working directory to where the HTML and GIF are
os.chdir(os.path.dirname(__file__))

# Start the server
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}/python.html")
    httpd.serve_forever()