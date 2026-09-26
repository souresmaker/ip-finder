from flask import Flask, request

app = Flask(__name__)

# This helper function wraps the raw number in centered, large display styling
def render_styled_page(ip_string):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>IP Display</title>
        <style>
            body, html {{
                height: 100%;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f5f5f7;
                font-family: 'Impact', 'Arial Black', sans-serif;
            }}
            .ip-box {{
                font-size: 8vw; /* Scale font dynamically with screen width */
                color: #1d1d1f;
                text-align: center;
                letter-spacing: 2px;
            }}
        </style>
    </head>
    <body>
        <div class="ip-box">{ip_string}</div>
    </body>
    </html>
    """

@app.route('/')
def get_my_ip():
    user_ip = request.remote_addr
    
    # 1. Check for standard proxy header chain
    forwarded = request.headers.get('X-Forwarded-For')
    if forwarded:
        ip_list = [ip.strip() for ip in forwarded.split(',')]
        if ip_list:
            # Fix: Takes the first text item out of the list to remove brackets
            user_ip = ip_list[0]
            
    # 2. Check for alternative real IP headers
    elif request.headers.get('X-Real-IP'):
        user_ip = request.headers.get('X-Real-IP').strip()

    # Pass the isolated IP into our styled HTML frame
    return render_styled_page(user_ip)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
