#!/usr/bin/env python3
"""
Alpha Games - Local Development Server
Run this to serve the game on localhost
"""

import http.server
import socketserver
import os
import webbrowser
import sys
from pathlib import Path

# Configuration
PORT = 8000
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom log format
        print(f"[{self.address_string()}] {format % args}")

def find_available_port(start_port=8000):
    """Find an available port starting from start_port"""
    import socket
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return None

def main():
    # Change to the directory containing this script
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("❌ Error: index.html not found!")
        print("Make sure you're running this script from the project directory.")
        sys.exit(1)
    
    # Find available port
    port = find_available_port(PORT)
    if port is None:
        print(f"❌ Error: Could not find an available port starting from {PORT}")
        sys.exit(1)
    
    try:
        # Create server
        with socketserver.TCPServer((HOST, port), CustomHTTPRequestHandler) as httpd:
            url = f"http://{HOST}:{port}"
            
            print("🎮 Alpha Games - Development Server")
            print("=" * 40)
            print(f"🌐 Server running at: {url}")
            print(f"📁 Serving files from: {script_dir}")
            print("=" * 40)
            print("🎯 Game Controls:")
            print("   • WASD or Arrow Keys: Move player")
            print("   • Space: Jump (Glass Bridge)")
            print("   • Mouse: Trace shapes (Honeycomb)")
            print("=" * 40)
            print("Press Ctrl+C to stop the server")
            print("")
            
            # Try to open browser automatically
            try:
                print("🚀 Opening browser...")
                webbrowser.open(url)
            except Exception as e:
                print(f"⚠️  Could not open browser automatically: {e}")
                print(f"Please manually navigate to: {url}")
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use!")
            print("Try closing other applications or use a different port.")
        else:
            print(f"❌ Server error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
