import os

def app(environ, start_response):
    # 1. Read your index.html file from the folder
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 2. Send a successful 200 OK web response header
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    
    # 3. Stream the HTML back to the browser
    return [html_content.encode('utf-8')]
