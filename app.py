from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_my_ip():
    # 1. Check for standard proxy header chain
    forwarded = request.headers.get('X-Forwarded-For')
    if forwarded:
        ip_list = [ip.strip() for ip in forwarded.split(',')]
        if ip_list:
            # Returns just the raw IP number string
            return f"{ip_list[0]}"
            
    # 2. Check for alternative real IP headers
    real_ip = request.headers.get('X-Real-IP')
    if real_ip:
        return f"{real_ip.strip()}"

    # 3. Fallback to basic remote connection address
    return f"{request.remote_addr}"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
