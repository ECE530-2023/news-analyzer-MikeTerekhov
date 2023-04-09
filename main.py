from bson import ObjectId
import pymongo
from pymongo import MongoClient
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import PyPDF2
from textblob import *
import openai
import re
import nltk
nltk.download('brown')
nltk.download('punkt')

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://terekhovhd:GreighT131@cluster0.g38mbdx.mongodb.net/?retryWrites=true&w=majority")
db = cluster['myFirstDatabase']
documents = db['documents']

openai.api_key = "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"

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
            "text": text,
            "summary": get_summary(text),
            "sentiment": get_sentiment(text)
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

def get_summary(text):
    prompt = (f"Please summarize the following text:\n{text}\n\n"
              "Summary:")
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=60,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    summary = response.choices[0].text.strip()
    # Remove any unwanted characters from the summary
    summary = re.sub(r'\n+', '\n', summary)
    summary = re.sub(r'\n$', '', summary)
    # Split summary into sentences and return the first three sentences
    summary_sentences = summary.split('. ')
    summary_3sentences = '. '.join(summary_sentences[:3]) + '.'
    return summary_3sentences

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

@app.route('/documents')
def document_list():
    docs = documents.find()
    return render_template('document_list.html', documents=docs)

@app.route('/view/<document_id>')
def view_document(document_id):
    doc = documents.find_one({'_id': ObjectId(document_id)})
    return render_template('view_document.html', document=doc)

@app.route('/NLP/<document_id>')
def NLP(document_id):
    doc = documents.find_one({'_id': ObjectId(document_id)})
    text = doc['text']
    word = request.args.get('word')
    if word:
        blob = TextBlob(text)
        word_count = blob.words.count(word)
        return render_template('NLP.html', document=doc, word_count=word_count, searched_word=word)
    else:
        sentiment = TextBlob(text).sentiment.polarity
        return render_template('NLP.html', document=doc, sentiment=sentiment)

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.run(debug=True)
