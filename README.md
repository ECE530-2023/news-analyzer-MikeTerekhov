# news-analyzer-MikeTerekhov
- built seperate REST APIs that allow the user to upload a PDF file, and then perform sentiment analysis on uploaded documents.
- stores all documents and their respective analysis in a MongoDB.
- Fully functioning frontend with HTML, CSS, and Javascript
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
  _id: ObjectId(),
  user_id: ObjectId(),
  document_id: ObjectId()
}
```
--------------------------------
Users:
```
{
    User storing : [
    {
        id: ObjectId(),
        name: String,
        email: String,
        password: String
    }
    ]
}
```
-----------------------------------------------
Documents:
```
{
    Document storing: [
    {   
    "name": filename,
    "type": "pdf",
    "text": text,
    "summary": get_summary(text),
    "sentiment": get_sentiment(text)   
    }
    ]
}
```




