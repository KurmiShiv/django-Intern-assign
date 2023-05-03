# django-Intern-assign

1.GET /api/works - This endpoint returns a list of all works, with the option to filter by work type or artist name. If no filters are provided, it will return a list of all works.

Query Parameters:

work_type - Optional. Filter works by type. Can be one of youtube, instagram, or other.
artist - Optional. Filter works by artist name. Matches partial names as well.
Example Usage:

2.GET /api/works - Returns a list of all works.
GET /api/works?work_type=youtube - Returns a list of all works of type 'Youtube'.
GET /api/works?artist=john - Returns a list of all works by artists whose name contains 'john' (e.g. 'John Smith', 'Johnny Cash', etc.).
POST /api/register - This endpoint allows a user to register by providing a username and password in the request body.

Request Body:

username - Required. The username for the new user.
password - Required. The password for the new user.
Example Usage:

POST /api/register

json
Copy code
{
    "username": "testuser",
    "password": "123123"
}
Returns a response indicating that the registration was successful.

That's it for the API endpoints in this example. Note that these endpoints are just examples and would need to be adapted to your specific use case and requirements.





