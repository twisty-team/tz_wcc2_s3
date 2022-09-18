# tz_wcc2_s3
TechZara WCC 2nd edition semaine 3

## Query form
Query should has this form to return result needed  
you can change page value to change result page  
if page is not specify, query by default return first page of result  
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
