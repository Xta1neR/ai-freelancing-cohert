# Topics for Today : 
HTTP → APIs → JSON → API keys and authentication → 
Python API requests → building your own API → connecting AI APIs.

## Task to do : 
- Create api_test.py and make one successful API request using Python.

<hr>

### HTTP/HTTPS
```
HTTP stands for Hypertext Transfer Protocol, while 
HTTPS stands for Hypertext transfer protocol secure. 

HTTP is the set of rules that allows your browser to communicate with the web server. 
For Example : 
    - We search "www.google.com" in the browser.
    - The browser sends a HTTP request to google server. 
    -  The server processes the request. 
    - The server then sends back the requested content or data.
    - The browser displays the received data. 

Meanwhile, HTTPS does the same work as the example above but it adds a TLS encryption 
layer to protect data in transit and authenticates the server. 
```
<b> HTTP Status code </b>
- 200 OK : ``` Request Successful ```
- 201 Created : ``` Resource Created Successfully ```
- 301 Moved Permanently : ``` Resource has moved to new URL ```
- 400 Bad Request : ``` Invalid Request ```
- 401 Unauthorized : ``` Authentication Required of user ```
- 403 Forbidden : ``` Access is not permitted ```
- 404 Not found : ``` Resource not found ```
- 500 Internal Server Error : ``` Server encountered an error ```

<b> HTTP Methods </b>
- ```GET``` : Retrieve Data from server
- ```POST```: Send data or create data in server
- ```PUT```: Replace an existing data from server
- ```PATCH```: Partially update data on server
- ```DELETE```: Delete data from server

<br>
<hr>

### APIs
```
API stands for Application Programming Interface. It helps two software to 
communicate with each other using a defined set of rules. 


For example, when you open a weather app:

1. The app requests weather data.
2. A weather API receives the request.
3. The weather service provides the relevant data.
4. The API returns the data to the app.
5. The app displays the temperature and forecast.
```
<b>What is an API Key ? </b>
Its a secret key used by API providers to identify or authorize an application. 



<hr>

### JSONs
```
JSON stands for JavaScript Object Notation. 
Its a lightweight format for storing and exchanging data between apps. 

For Example : 
    {
        "name": "Rituraj",
        "age": 23,
        "city": "Delhi",
        "is_developer": true
    }

