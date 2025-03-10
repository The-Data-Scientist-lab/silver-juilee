from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

PHOTO_DIR = os.path.join(app.static_folder, 'images')

if not os.path.exists(PHOTO_DIR):
    os.makedirs(PHOTO_DIR)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/gallery')
def gallery():
    photos = os.listdir(PHOTO_DIR) if os.path.exists(PHOTO_DIR) else []
    return render_template('index.html', photos=photos)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(PHOTO_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)