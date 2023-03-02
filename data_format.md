#Explanation

For our database structure design we have chosen to go with MongoDB database structure due to the nature of our input. Due to the fact that the main entity of our project is a document, it would be very difficult to store this information in a table based format such as SQL. Due to the fact that we are planning on splitting up the document into paragraphs and images, it would be easier to use a JSON format to store and query that information.

#schema
-----------------------------------

{
  _id: ObjectId(),
  user_id: ObjectId(),
  document_id: ObjectId()
}

--------------------------------

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
-----------------------------------------------
{
    Document storing: [
    {
        _id: ObjectId(),
        name: String,
        type: String,
        size: Number,
        created_at: Date
    }
    ]
}

----------------------------------------
{
    Document Analysis : [
    {
        _id: ObjectId(),
        document_id: ObjectId(),
        text: String,
        language: String,
        sentiment: String,
        entities: [{
            name: String,
            type: String,
            relevance: Number
    }
    ]   
}


