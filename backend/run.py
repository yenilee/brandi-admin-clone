from app import create_app

IP           = '192.168.7.40'
REVIEW_IP    = '10.250.2.195'
LOCALHOST    = 'localhost'
YEEUN        = '10.250.2.93'
CAFE         = '172.30.1.33'
WECODE       = '10.58.3.11'
WECODE_YEEUN = '10.58.5.11'
HOME         = '192.168.35.167'

if __name__ == "__main__":
    app = create_app()
    
    app.run(host = LOCALHOST, port = 5000)