from app import create_app

IP        = '192.168.7.40'
REVIEW_IP = '10.250.2.195'
LOCALHOST = 'localhost'

if __name__ == "__main__":
    app = create_app()
    app.run(host = REVIEW_IP, port = 5000)
