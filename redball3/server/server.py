import http.server
import socketserver
import json
import random

PORT = 5000

count = 0
actions = ["p","X","Q","E","W","S","A","D","Z","x","q","e","w","s","a","d","z"]

class CrossDomainPolicyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global count
        print(self.path)
        if self.path == "/crossdomain.xml":
            self.send_response(200)
            self.send_header("Content-type", "application/xml")
            self.end_headers()
            self.wfile.write(b"<?xml version='1.0'?><cross-domain-policy><allow-access-from domain='*' /></cross-domain-policy>")
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        command = ""
        for i in range(random.randint(3, 9)):
            command += random.choice(actions)
        print(count)
        count += 1
        if(count < 100):
            command = "1"+command
        else:
            command = "0"+command
        self.wfile.write(bytes(command,'utf-8'))

with socketserver.TCPServer(("", PORT), CrossDomainPolicyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()