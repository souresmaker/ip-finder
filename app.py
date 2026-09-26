from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_my_ip():
    # Checks the cloud forwarding header first, then falls back to local network
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return f"Your IP Address is: {user_ip}"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
