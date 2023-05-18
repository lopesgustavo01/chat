from app import app, io
import os

if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    io.run(app, host='0.0.0.0', port=port)
