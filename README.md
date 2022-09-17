# tz_wcc2_s3
TechZara WCC 2nd edition semaine 3

## Query form
change page value to change page 
default 
```sh
{
    exchanges {
        ...
    }
}
```
will return first page
```sh
{
  exchanges(page:1) {
      count
    	currentPage
    	totalPages
      next
      prev
      results {
        id
        toyToChange
        desiredToy
        active
        owner {
          id
          name
          contact
        }
        pictures {
          id
          imageUrl
        }
  	}
	}
}
```
##Query response
```json
{
  "data": {
    "exchanges": {
      "count": 21,
      "currentPage": 1,
      "totalPages": 3,
      "next": "http://127.0.0.1:8000/graphql#query={exchanges(page:2){count currentPage totalPages next prev results{id toyToChange desiredToy active owner{id name contact} pictures{id imageUrl}}}}",
      "prev": null,
      "results": [
			{
			  "id": "21",
			  "toyToChange": "fqqdfdq",
			  "desiredToy": "fdqfdqf",
			  "active": true,
			  "owner": {
			    "id": "2",
			    "name": "jose",
			    "contact": "+261332514778"
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
