from app import app
import os

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run('127.0.0.1', port=port)