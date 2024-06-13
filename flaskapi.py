from flask import Flask, request, jsonify, send_file
import brotli
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
COMPRESSED_FOLDER = 'compressed'
DECOMPRESSED_FOLDER = 'decompressed'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)
os.makedirs(DECOMPRESSED_FOLDER, exist_ok=True)

@app.route('/compress-file', methods=['POST'])
def compress_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        original_size = os.path.getsize(file_path)
        with open(file_path, 'rb') as f:
            data = f.read()
        compressed_data = brotli.compress(data)
        compressed_path = os.path.join(COMPRESSED_FOLDER, file.filename + '.br')
        with open(compressed_path, 'wb') as f:
            f.write(compressed_data)
        compressed_size = os.path.getsize(compressed_path)
        return jsonify({
            "original_size": original_size,
            "compressed_size": compressed_size,
            "compressed_file_url": compressed_path
        })
    return "No file uploaded", 400

@app.route('/uncompress-file', methods=['POST'])
def uncompress_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(COMPRESSED_FOLDER, file.filename)
        file.save(file_path)
        compressed_size = os.path.getsize(file_path)
        with open(file_path, 'rb') as f:
            compressed_data = f.read()
        data = brotli.decompress(compressed_data)
        decompressed_path = os.path.join(DECOMPRESSED_FOLDER, file.filename.replace('.br', ''))
        with open(decompressed_path, 'wb') as f:
            f.write(data)
        decompressed_size = os.path.getsize(decompressed_path)
        return jsonify({
            "compressed_size": compressed_size,
            "decompressed_size": decompressed_size,
            "decompressed_file_url": decompressed_path
        })
    return "No file uploaded", 400

if __name__ == '__main__':
    app.run(debug=True)
