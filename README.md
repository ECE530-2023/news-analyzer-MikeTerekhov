# news-analyzer-MikeTerekhov
This repository contains my PDF analysis project, along with examples of experimenting with queues/threading aswell as an example of making my own pip install package. As a part of the class I also chose to try and experiment with create the same app using React JS. At the moment, it only contains a method of using the Google authentication API, without any other applications.
-------------------------------------------------------------------------
# Installation
To intall and get the main Python Flask server running simply clone this github repo, install all dependendncies, should cover eveything. Then run main.py and launch local host server ip adress in a browser. Note OpenAI API wont display the summary since I have not added a credit card to my account. 
 - To go to NL analsysis, click on NLP letters on page where all text is shown!
-------------------------------------------------------------------------
- built seperate REST APIs to :
    - upload a PDF File
    - obtain sentiment of file
    - seperate web-scraping features
    - ChatGPT implementation

- stores all documents and their respective analysis in a MongoDB.

- Fully functioning frontend with HTML, CSS, and Javascript
-------------------------------------------------------------------------
# List of APIs
- upload
    - upload a PDF and checks the correct input
    - saving to Mongo DB happens in here as well
    - uses allowed_file fucntion to check file format
- extract text
    - scrapes the PDF and extracts all containing text and returns it
- get summary
    - utilizes OpenAI API to prompt the model to summarize the text of the respective document
    - CREDIT CARD must be added to OpenAI accountt o make it functional
    - cuts down summary to three sentances
- get sentiment
    - Uses TextBlob Python library to optain sentiment from text
- document list
    - displays all uploaded documents
- document view
    - renders page that shows link to NLP and the text that was extracted
- NLP
    - renders page that will show sentiment analysis, GPT summary, and also creates a feature where you can search how many times a certain word appears in the respective text
- Sentiment def
    - renders a page that shows the TextBlob website defentition for the sentiment value given that gives user insight on what the meaning of the analysis is 


-------------------------------------------------------------------------
# MongoDB

- For our database structure design we have chosen to go with MongoDB database structure due to the nature of our input. 
- Due to the fact that the main entity of our project is a document, it would be very difficult to store this information in a table based format such as SQL. 
-Due to the fact that we are planning on splitting up the document into paragraphs and images, it would be easier to use a JSON format to store and query that information.

# Why MongoDB?

- Mongo is much less structured. This will easier allow to altercation and addition of data collected from out documents
- Allows for more flexibility with sentiment analysis section by potentially allowing user to select different portions of text that they want to analyze
- due to many different document types/structures, rigid table structure is difficult to fill it in effectively

# Schema
```
{
            "name": filename,
            "type": "pdf",
            "text": text,
            "summary": summary,
            "sentiment": sentiment
}
```
-------------------------------------------------------------------------
# Goals of sentiment analysis & web-scraping
- extract all text from PDF
- be able to obtain the overall sentiment of the document
- search and find the occurences of a certain keyword in a document
- ChatGPT summary for the document (in progress)
- Converse with ChatGPT about the text
