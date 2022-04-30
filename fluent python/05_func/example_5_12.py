

import bobo

@bobo.query('/')
def hello(person):
    return 'hello %s'%person

   
'''
gongyan@Franck 05_func % curl -i http://localhost:8080/
HTTP/1.0 403 Forbidden
Date: Sat, 30 Apr 2022 07:48:34 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: text/html; charset=UTF-8
Content-Length: 103

<html>
<head><title>Missing parameter</title></head>
<body>Missing form variable person</body>
</html>
gongyan@Franck 05_func % curl -i http://localhost:8080/?person=jim 
HTTP/1.0 200 OK
Date: Sat, 30 Apr 2022 07:48:57 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: text/html; charset=UTF-8
Content-Length: 9

hello jim%  
'''
