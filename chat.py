from app import io
import os

if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    io.run(host='0.0.0.0', port=port)
