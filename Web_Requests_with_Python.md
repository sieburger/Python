Web_Requests_with_Python.md

***

## Introduction

The Internet is an enormous source of data and, often, websites will offer a RESTful [API](https://en.wikipedia.org/wiki/Application_programming_interface) endpoints (URLs, URIs) to share data via HTTP requests. HTTP requests are composed of methods like GET, POST, PUT, DELETE, etc. to manipulate and access resources or data. Often, websites require a registration process to access RESTful APIs or offer no API at all. So, to simplify the process, we can also download the data as raw text and format it. For instance, downloading content from a personal blog or profile information of a GitHub user without any registration. This guide will explain the process of making web requests in python using `Requests` package and its various features.

## Prerequisites

1. Python setup: Download and install the python setup from [python.org](https://www.python.org/downloads/) or you can run python in browser with [jupyter notebook](https://jupyter.org/).
2. Request Package: Use python package manager (pip) command in the terminal (command prompt) to install packages.

```python
pip3 install requests
```

python

> Use `pip` for python 2 (until python 3.4). Python also offers [Virtualenv](https://virtualenv.pypa.io/en/stable/) to manage the dependencies and development environments separately, across multiple applications.

## Making a Get Request

In order to make a REST call, the first step is to import the python `requests` module in the current environment.

```python
import requests                                 # To use request package in current program 
response = requests.get("www.dummyurl.com")     # To execute get request 
```

python

> Python also provides a way to create alliances using the `as` keyword.

```python
import requests as reqs 
response = reqs.get('https://www.google.com') 
```

python

To make the first request, we will be using [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API which provides JSON response for specific item like posts, todos, and albums. So, the `/todos/1` API will respond with the details of a TODO item.

```python
url = 'https://jsonplaceholder.typicode.com/todos/1' 
response = requests.get(url)        # To execute get request 
print(response.status_code)     # To print http response code  
print(response.text)            # To print formatted JSON response 
```

python

The execution of above snippet will provide the result:

```json
200 
{ 
  "userId": 1, 
  "id": 1, 
  "title": "delectus aut autem", 
  "completed": false 
} 
```

json

The status code `200` means a successful execution of request and `response.content` will return the actual JSON response of a TODO item.

> There are many [public APIs](https://github.com/toddmotto/public-apis) available to test REST calls. You can also use [Postman Echo](https://docs.postman-echo.com/#intro) or [mocky](https://www.mocky.io/) to return customized responses and headers as well as adding a delay to the generated dummy link.

## POST Request

Post requests are more secure because they can carry data in an encrypted form as a message body. Whereas GET requests append the parameters in the URL, which is also visible in the browser history, SSL/TLS and HTTPS connections encrypt the GET parameters as well. If you are not using HTTPs or SSL/TSL connections, then POST requests are the preference for security.
A dictionary object can be used to send the data, as a key-value pair, as a second parameter to the `post` method.

```python
data = {'title':'Python Requests','body':'Requests are awesome','userId':1} 
response = requests.post('https://jsonplaceholder.typicode.com/posts', data) 
print(response.status_code) 
print(response.text) 
```

python

This dummy post request will return the attached `data` as response body:

```json
201 
{ 
  "title": "Python Requests", 
  "body": "Requests are awesome", 
  "userId": "1", 
  "id": 101 
} 
```

json

> POST requests have no restriction on data length, so they’re more suitable for files and images. Whereas GET requests have a limit of 2 kilobytes (some servers can handle 64 KB data) and GET only allows ASCII values.
>
> Just like `post`, `requests` also support other methods like `put`, `delete`, etc. Any request can be sent without any data and can define empty placeholder names to enhance code clarity.

```python
response = req.post('https://jsonplaceholder.typicode.com/posts', data = None, json = dictionaryObject) 
print(response.json())      # output: {'id': 101} 
```

python

In this case where `data` is set as `None`, this can be skipped because it happened automatically due to default values.

## Response Types

The response object can be parsed as string, bytes, JSON, or raw as:

```python
print(response.content)           # To print response bytes 
print(response.text)              # To print unicode response string 
jsonRes = response.json()         # To get response dictionary as JSON 
print(jsonRes['title'] , jsonRes['body'], sep = ' : ')  # output: Python Requests : Requests are awesome 
```

python

Reading the response as a raw value allows us to read specific number of bytes and to enable this, set `stream = True` as a parameter in the request method.

```python
data = {'title':'Pyton Requests','body':'Requests are qwesome','userId':1} 
response = req.post('https://jsonplaceholder.typicode.com/posts', data, stream = True) 
print(response.raw.read(30))     # output: b'{\n  "title": "Python Requests"' 
```

python

> To enable stream, the `stream` placeholder has to be mentioned specifically because it is not a required argument.

You can also use `iter_content` method which automatically decodes `gzip` files.

```python
response.iter_content(chunk_size=1024) 
```

python

## Authentication

The process of authentication is required by many APIs to allow access to user specific details. Requests support various types of authentication, such as:

- Basic Auth: This transfers the authentication details as `base64` encoding (text as bytes), meaning there is no encryption and security. It is suitable for HTTPs or SSL/TSL enabled connections where security is inbuilt.

```python
# Open github API to test authentication 
from requests.auth import HTTPBasicAuth     
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('userName', 'password')) 
 
# or shortcut method 
requests.get('https://api.github.com/user', auth=('user', 'pass'))  
```

python

- Digest Auth: This transfers the credentials in an encrypted form by applying a hash function on credentials, HTTP method, nonce (one-time number, provided by server), and the requested URI. Hence, it is more secured while making HTTP calls.

```python
from requests.auth import HTTPDigestAuth 
response = reqs.get('https://postman-echo.com/digest-auth', auth=HTTPDigestAuth('postman', 
'password')) 
```

python

> Digest Auth can still be hacked and HTTPs or SSL/TSL security should be preferred over digest authentication.

## Headers

A header contains information about the client (type of browser), server, accepted response type, IP address, etc. Headers can be customized for the source browser ([user-agent](https://en.wikipedia.org/wiki/User_agent)) and content-type. They can be viewed using `headers` property as:

```python
headers = {'user-agent': 'customize header string', 'Content-Type': 'application/json; charset=utf-8'}  
response = requests.get(url, headers=headers)   # modify request headers 
print(response.headers)                         # print response headers 
print(response.headers['Content-Type'])         # output: application/json; charset=utf-8 
```

python

## Cookies

Cookies are small pieces of data stored on the client (browser) side and are often used to maintain a login session or to store user IDs. Both the client and server can send cookies. Use the `cookies` property to send and access cookies.

```python
cookie = {'username':'Pavneet'} 
response = reqs.get('https://postman-echo.com/cookies/set',cookies = cookie)   # send cookie 
print(response.text)    # output: {"cookies":{"username":"Pavneet"}} 
```

python

> Use `response.cookies` to access the cookies from server response

## Timeout and Redirection

- Timeout: It allows `requests` to terminate any request, if there is no response within the set timeout duration. This will avoid any indefinite waiting state, in case there's no response from server.

```python
requests.get('https://github.com/', timeout=0.50) 
```

python

- Redirection: Requests provide the `url` property to track redirected URLs.

```python
response = requests.get('http://github.com/', allow_redirects=True) 
response.url
```

python

> To disable redirection, set the `allow_redirects` parameter to `False`. By default it is set to`True`.

## Key Points

- Sending sensitive data, such as password, over GET requests with HTTPs or SSL/TSL is considered very poor practice. While it cannot be intercepted, the data would be logged in serverlogs as plain text on the receiving HTTPS server and quite possibly also in browser history. It is probably also available to browser plugins and, possibly, other applications on the client computer.
- Lists of other supported parameters like [proxies, cert, and verify](http://docs.python-requests.org/en/master/_modules/requests/api/) are supported by Requests.
- Always mention specific exceptions first over general exceptions, to catch any specific exception:

```python
try: 
    response = requests.get(url,timeout=3) 
    response.raise_for_status()                 # Raise error in case of failure 
except requests.exceptions.HTTPError as httpErr: 
    print ("Http Error:",httpErr) 
except requests.exceptions.ConnectionError as connErr: 
    print ("Error Connecting:",connErr) 
except requests.exceptions.Timeout as timeOutErr: 
    print ("Timeout Error:",timeOutErr) 
except requests.exceptions.RequestException as reqErr: 
    print ("Something Else:",reqErr) 
```

***

[source](https://www.pluralsight.com/guides/web-scraping-with-request-python)