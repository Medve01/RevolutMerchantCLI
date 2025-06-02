#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

def format_headers(headers):
    return {k: v for k, v in headers.items() if k.lower() not in ['host', 'content-length']}

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n=== New Request at {timestamp} ===")
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    print(f"Path: /{path}")
    print(f"Query Params: {dict(request.args)}")
    print(f"Headers: {json.dumps(format_headers(dict(request.headers)), indent=2)}")
    
    if request.is_json:
        print(f"Body: {json.dumps(request.get_json(), indent=2)}")
    elif request.data:
        try:
            print(f"Body: {json.dumps(json.loads(request.data), indent=2)}")
        except:
            print(f"Body: {request.data.decode()}")
    
    print("=" * 50)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("Starting webhook listener on http://localhost:8000")
    print("Press Ctrl+C to stop")
    app.run(host='0.0.0.0', port=8000) 