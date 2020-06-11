from app import create_app

IP        = '192.168.7.40'
REVIEW_IP = '10.250.2.195'
LOCALHOST = 'localhost'
YEEUN     = '10.250.2.94'
CAFE      = '192.168.7.39'
WECODE    = '10.58.3.11'

if __name__ == "__main__":
    app = create_app()

    app.run(host = YEEUN, port = 5000)

