#!/usr/bin/python3

from app import app, app_port

if __name__ == '__main__':
    app.run('0.0.0.0', port=app_port)
