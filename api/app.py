### FILE 1: api/index.py ###
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        CLIENT_ID = '1336407521866289172'
        
        # Bot permissions (8 = Administrator)
        PERMISSIONS = '8'
        
        # Scopes needed for bot
        SCOPES = 'bot%20applications.commands'
        
        # Build Discord OAuth URL
        discord_url = f'https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&permissions={PERMISSIONS}&scope={SCOPES}'
        
        # Send 301 redirect
        self.send_response(301)
        self.send_header('Location', discord_url)
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        return

