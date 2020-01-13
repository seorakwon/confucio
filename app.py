from flask import Flask, render_template
from flask import Flask
import src.predict as p
import os
from werkzeug.utils import secure_filename
from flask import request
from flask import send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/seora/github/proyecto-IH/fotos' 

@app.route('/fotos/<path:path>')
def send_js(path):
    return send_from_directory('fotos', path)

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def uploader():
 if request.method == 'POST':
 
  f = request.files['archivo']
  filename = secure_filename(f.filename)
  #image = f.save("/home/seora/github/proyecto-IH/output/upload_folder/predict.jpg")
  #pred = p.get_prediction("/home/seora/github/proyecto-IH/output/upload_folder/predict.jpg")
  image = f.save("/home/seora/github/proyecto-IH/fotos/predict.jpg")
  pred = p.get_prediction(("/home/seora/github/proyecto-IH/fotos/predict.jpg"))
  return render_template("predict.html",pred=pred)



if __name__ == '__main__':
    app.run(debug=True)





