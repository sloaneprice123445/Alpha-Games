#!/usr/bin/env python3
"""
Alpha Games Local Server
A simple HTTP server to run the Alpha Games web application locally.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def main():
    # Change to the directory containing this script
    os.chdir(Path(__file__).parent)
    
    # Configuration
    PORT = 8002
    HOST = "localhost"
    
    # Create server
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
            print(f"🎮 Alpha Games Server Starting...")
            print(f"📡 Server running at: http://{HOST}:{PORT}")
            print(f"🌐 Opening game in your default browser...")
            print(f"⏹️  Press Ctrl+C to stop the server")
            
            # Open the game in the default web browser
            webbrowser.open(f"http://{HOST}:{PORT}")
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped.")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use.")
            print(f"💡 Try closing other applications or use a different port.")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
