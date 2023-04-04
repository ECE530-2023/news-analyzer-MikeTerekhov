# app.py
from bson import ObjectId
import pymongo
from pymongo import MongoClient
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import PyPDF2

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://terekhovhd:GreighT131@cluster0.g38mbdx.mongodb.net/?retryWrites=true&w=majority")
db = cluster['myFirstDatabase']
documents = db['documents']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        text = extract_text(file_path)
        doc = {
            "name": filename,
            "type": "pdf",
            "text": text
        }
        documents.insert_one(doc)
        return text
    else:
        return 'Invalid file type'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf'}

def extract_text(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text
    
@app.route('/documents')
def document_list():
    docs = documents.find()
    return render_template('document_list.html', documents=docs)

@app.route('/view/<document_id>')
def view_document(document_id):
    doc = documents.find_one({'_id': ObjectId(document_id)})
    return render_template('view_document.html', document=doc)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    doc_id = request.form['document_id']
    doc = documents.find_one({'_id': ObjectId(doc_id)})
    text = doc['text']
    matches = [word for word in text.split() if query.lower() in word.lower()]
    return render_template('search_results.html', query=query, matches=matches)

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.run(debug=True)
