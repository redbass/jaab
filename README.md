# JAAB (Just another address book)

This application is a basic example of Flask and Angular integration. The backend 
  is using TinyDB module to store in file (`resource/data.json`) a small collection
  of companies and employees (for each of them). 


## How to start the app:
To run the app follow the next steps:

- Install python dependencies:
    pip install -r requirements.txt
- Populate base db:
    python bin/populate_db.py
- Run application:
    python app.py
    
To see the application running open a browser at the address
    http://localhost:5000/#/companies

  
The API are: 

- GET - http://localhost:5000/api/v1/company - Get companies
- GET - http://localhost:5000/api/v1/company/<id> - Get company
- POST - [http://localhost:5000/api/v1/company/<id>/employee]() - add a new employee
- POST - [http://localhost:5000/api/v1/company/<id>/employee/<eid>]() - update an employee
- DELETE - [http://localhost:5000/api/v1/company/<id>/employee]() - delete an employee
- GET - [http://localhost:5000/api/v1/company/<id>/employee]() - get an employee

## Final consideration
Probably Angular is not the quickest solution for this type of project, is a
 bit overkill. But is a good way to explain the integration between the two
 technologies and how to separate frontend and backend blocks.
 For time reasons there are no frontend tests, and api have just little coverage.
 Also the error API handling can be improved, returning nice HTTP statuses with
 a meaningful message description. 