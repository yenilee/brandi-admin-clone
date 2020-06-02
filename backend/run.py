from app import create_app

IP = '192.168.7.40'

if __name__ == "__main__":
    app = create_app()
    app.run(host = 'localhost', port = 5000)
