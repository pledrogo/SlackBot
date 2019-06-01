from routes import application
import os

if __name__ == '__main__':
    application.debug = True
    port = int(os.environ.get("WEBSERVER_PORT", 5000))
    application.run(host='0.0.0.0', port=port)