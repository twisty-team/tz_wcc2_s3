# Ndao atakalo
TechZara WCC 2nd edition week 3

A GraphQL API that allow people to exchange their toys

## Prerequisites
You'll need python 3 in order to run the project.
To install the dependencies, run (preferably in a virtual environment):
```sh
pip3 install -r requirements.txt
```

## How to run
Before the first run, you'll need to setup the database.
```sh
python3 manage.py migrate
```
Then, run the project by typing in the terminal :
``` sh
python3 manage.py runserver
```
The server will be launch on 127.0.0.1:8000 by default but you can specify
a host and a port as following :
```sh
python3 manage.py runserver 0.0.0.0:3000
```
Open a browser at [127.0.0.1:8000/graphql](127.0.0.1:8000/graphql)(graphiql) or use Postman to test the API.


## API reference

### Endpoints
All queries are made at [localhost:8000/graphql](http://localhost:8000/graphql) using `POST` for mutation and `GET` for simple query.

### Authentication
There is actually no authentication/authorization implemented.

### Errors
Errors are returned following the GraphQL spec.

### Queries 
- createExchange(`usserName`, `contact`, `desiredToy`, `toyToChange`)
- deactivateExchange(`id`)
- paginatedExchange(`page`, `pageSize`)

## Query form
Query should has this form to return result needed  
you can change page value to change result page  
if page is not specified, query by default return first page of result  
```sh
{
  paginatedExchanges(page: 1)
  {
    count
    pageSize
    currentPage
    totalPages
    hasNext
    hasPrev
    exchanges
    {
      id
      toyToChange
      desiredToy
      active
      owner 
      {
        id
        name
        contact
      }
      pictures
      {
        id
        imageUrl
      }
  	}
  }
}
```
You can specify pageSize to configure exchange per page  
you should add parameter to the query like this  
```sh
{
  paginatedExchanges(pageSize:2 page: 1)
  {
      ........
  }
}
```
## Query response
Query json response will have this form
```json
{
  "data": {
    "paginatedExchanges": {
      "count": 20,
      "pageSize": 10,
      "currentPage": 1,
      "totalPages": 2,
      "hasNext": true,
      "hasPrev": false,
      "exchanges": [
        {
          "id": "20",
          "toyToChange": "test",
          "desiredToy": "test",
          "active": true,
          "owner": {
            "id": "1",
            "name": "owner1",
            "contact": "+261324711525"
          },
          "pictures": []
        },
        {
          "...": "..."
        }
      ]
    }
  }
}
```

## Authors

* [tbgracy](https://github.com/tbgracy)

* [rhja](https://github.com/radoheritiana)