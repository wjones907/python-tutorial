# Requests
#   - send
#   -
#
# Requests allow you to send HTTP/1.1 requests.
#
# Requests is an Apache2 Licensed HTTP library, written in Python, for human beings
#
#
# You can add headers, form data, multipart files, and parameters with simple
# Python dictionaries, and access the response data in the same way.
#
# use http://httpbin.org/ as a sample web site
# 
# It supports most of the common HTTP verbs and mostly return the variables you
# send in, which is sometimes very useful when you are writing a (HTTP) script.




import requests

# MAKE A REQUEST
# Get a webpage, this creates a Response object called "r"
r = requests.get('https://github.com/timeline.json')




# RESPONSE CODE
# We can check the response status code, and do a status code lookup with the dictionary look-up object.
r = requests.get('https://github.com/timeline.json')
r.status_code
# >>200

r.status_code == requests.codes.ok
# >>> True

requests.codes['temporary_redirect']
# >>> 307

requests.codes.teapot
# >>> 418

requests.codes['o/']
# >>> 200















