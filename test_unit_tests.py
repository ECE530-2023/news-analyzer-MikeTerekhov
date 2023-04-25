import pytest

from main import *
import numpy as np
import logging
import sys
import json
# Unit tests for all API modules

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

class TestClass:

    # test_unit_tests.py

    def test_upload(self):
        logger.info('Started uploader tests')
        with app.test_client() as client:
            token = 'my_api_key_1'
            data = {'name': 'Document 1'}
            headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
            response = client.post('/upload', json=data, headers=headers)
            assert response.status_code == 201
    
    def test_document_list():
        logger.info('Started document list tests')
        with app.test_client() as client:
            # Create a fake document in the MongoDB collection for testing
            documents.insert_one({'title': 'Test Document', 'content': 'This is a test document.'})
            
            # Send a GET request to the '/documents' endpoint
            response = client.get('/documents')
            
            # Check that the response status code is 200
            assert response.status_code == 200
            
            # Check that the rendered template contains the title of the fake document
            assert b'Test Document' in response.data
            
            # Check that the rendered template contains the content of the fake document
            assert b'This is a test document.' in response.data
            
            # Remove the fake document from the MongoDB collection
            documents.delete_one({'title': 'Test Document'})

    def test_nlp():
        logger.info('Started NLP tests')
        with app.test_client() as client:
            # Create a fake document in the MongoDB collection for testing
            documents.insert_one({'_id': ObjectId(), 'text': 'This is a test document.'})
            
            # Send a GET request to the '/NLP/<document_id>' endpoint without a search word
            response = client.get('/NLP/{}'.format(str(documents.find_one()['_id'])))
            
            # Check that the response status code is 200
            assert response.status_code == 200
            
            # Check that the rendered template contains the document text
            assert b'This is a test document.' in response.data
            
            # Check that the rendered template contains the sentiment analysis result
            assert b'Sentiment Analysis' in response.data
            
            # Send a GET request to the '/NLP/<document_id>' endpoint with a search word
            response = client.get('/NLP/{}?word=test'.format(str(documents.find_one()['_id'])))
            
            # Check that the response status code is 200
            assert response.status_code == 200
            
            # Check that the rendered template contains the search word count
            assert b'Word Count' in response.data
            
            # Check that the rendered template contains the search word
            assert b'Searched Word: test' in response.data
            
            # Remove the fake document from the MongoDB collection
            documents.delete_one({'text': 'This is a test document.'})
