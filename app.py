from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_my_ip():
    # Grabs the cloud forwarding header chain safely
    raw_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    # Splits the list by the comma, takes the 1st value [0], and cleans spaces
    user_ip = raw_ip.split(',')[0].strip()
    return f"Your IP Address is: {user_ip}"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
