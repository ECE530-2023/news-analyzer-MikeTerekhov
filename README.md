# news-analyzer-MikeTerekhov
- added Github Actions 
- created majority of function stubs
- implemented a test file with a test class for secure_file_uploader
- created a txt file with errors and their descriptions 
- Unit tests are created in test_unit_tests file for all API modules
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
        _id: ObjectId(),
        name: String,
        type: String,
        size: Number,
        uploaded_at: Date
    }
    ]
}
```
----------------------------------------
Document Analysis:
```
{
    Document Analysis : [
    {
        _id: ObjectId(),
        document_id: ObjectId(),
        keywords: String,
        text: String,
        language: String,
        sentiment: String,
        entities: [{
            name: String,
            type: String,
            relevance: Number
            ]
    }
    ]   
}
```



