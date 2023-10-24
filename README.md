# PythonRESTAPI_Flask

Setup and Running the Project
1. Install Dependencies:
Install all of the required packages from packages.txt, Any compatible versions should be fine, the versions listed were the ones used during the development of this project. 
2. Setting Up the Database:
Navigate to the project directory using command prompt/file explorer/any other method
Make sure that the line db.create.all() in main.py is not commented out
Run the script to initialize the database with 
`python main.py`
3. Running Tests:
Open a new instance of command prompt in the project directory
Comment out the line db.create.all() in main.py
Run the test script to execute the tests (You can change the tests and make your own)
`python test.py`




This project was made using the following

Flask -> Lightweight web framework for Python to build and run a web server

Flask-RESTful -> Extension for flask that lets you build REST API

SQLite -> Lightweight Database. Used for video storage

SQLAlchemy -> Object Relational Mapper that lets you build REST API

Python Request Module -> Allows you to make http requests to your api, simulating client server interactions

It supports the following operations:

CRUD Operations
Create   ->  (put)
Retreive ->  (get)
Update   ->  (patch)
Delete   ->  (delete)