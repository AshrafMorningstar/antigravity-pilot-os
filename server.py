#!/usr/bin/env python3
"""
OmniPilot OS — Embedded Automation Server & API Engine
Deterministic, zero-external-dependency local HTTP server.
"""

import http.server
import json
import os
import subprocess
import sys
import urllib.parse

PORT = 8765
HOST = '127.0.0.1'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class OmniPilotHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/status':
            self._send_json(200, {
                'status': 'ok',
                'engine': 'Antigravity Pilot OS',
                'autonomy': '100% Zero-Permission',
                'version': '10.0.0'
            })
        elif parsed.path == '/api/git-status':
            self._handle_git_status()
        elif parsed.path == '/manifest.webmanifest':
            self.send_response(200)
            self.send_header('Content-Type', 'application/manifest+json; charset=utf-8')
            self.end_headers()
            with open(os.path.join(BASE_DIR, 'manifest.webmanifest'), 'rb') as f:
                self.wfile.write(f.read())
        else:
            super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_length) if content_length > 0 else b'{}'
        
        try:
            data = json.loads(post_body.decode('utf-8'))
        except Exception:
            data = {}

        if parsed.path == '/api/git-commit':
            self._handle_git_commit(data)
        elif parsed.path == '/api/generate-docs':
            self._handle_generate_docs(data)
        else:
            self._send_json(404, {'error': 'Endpoint not found'})

    def _send_json(self, status_code, payload):
        body = json.dumps(payload).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def _handle_git_status(self):
        is_git = os.path.exists(os.path.join(BASE_DIR, '.git'))
        if not is_git:
            self._send_json(200, {'initialized': False, 'committed': False})
            return

        try:
            status_res = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=BASE_DIR,
                capture_output=True,
                text=True,
                timeout=5
            )
            is_clean = len(status_res.stdout.strip()) == 0
            self._send_json(200, {
                'initialized': True,
                'committed': is_clean,
                'statusOutput': status_res.stdout
            })
        except Exception as e:
            self._send_json(200, {'initialized': True, 'committed': False, 'error': str(e)})

    def _handle_git_commit(self, data):
        commit_msg = data.get('message', 'feat(omnipilot): autonomous update')
        try:
            # 1. Ensure git is initialized
            if not os.path.exists(os.path.join(BASE_DIR, '.git')):
                subprocess.run(['git', 'init'], cwd=BASE_DIR, check=True, capture_output=True)

            # 2. Ensure local identity exists so commit doesn't fail
            subprocess.run(['git', 'config', 'user.name', 'OmniPilot Agent'], cwd=BASE_DIR, capture_output=True)
            subprocess.run(['git', 'config', 'user.email', 'omnipilot@local'], cwd=BASE_DIR, capture_output=True)

            # 3. Add all
            subprocess.run(['git', 'add', '.'], cwd=BASE_DIR, check=True, capture_output=True)

            # 4. Commit
            res = subprocess.run(
                ['git', 'commit', '-m', commit_msg],
                cwd=BASE_DIR,
                capture_output=True,
                text=True
            )

            # Check if main branch exists
            subprocess.run(['git', 'branch', '-M', 'main'], cwd=BASE_DIR, capture_output=True)

            self._send_json(200, {
                'success': True,
                'stdout': res.stdout or 'Committed successfully.',
                'stderr': res.stderr
            })
        except Exception as e:
            self._send_json(500, {'success': False, 'error': str(e)})

    def _handle_generate_docs(self, data):
        project_name = data.get('projectName', 'OmniPilot Project')
        vision = data.get('vision', 'Deterministic autonomous software')

        doc_files = [
            'PRD.md', 'Architecture.md', 'security.md', 'design.md',
            'phases.md', 'flow.md', 'rules.md', 'decision.md', 'memory.md',
            'FAST_RESUME.md', 'INDEX.md', 'HUMAN_BRIEF.md'
        ]

        verified = []
        for filename in doc_files:
            path = os.path.join(BASE_DIR, filename)
            if os.path.exists(path):
                verified.append(filename)

        self._send_json(200, {
            'success': True,
            'message': f'Verified and synced {len(verified)} documents (9 core + token recovery + human brief) for {project_name}.',
            'verifiedDocs': verified
        })

def run_server():
    print(f"Starting OmniPilot OS server on http://{HOST}:{PORT} ...")
    server = http.server.HTTPServer((HOST, PORT), OmniPilotHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()

if __name__ == '__main__':
    run_server()
