To start building peach xml file:

1. Use BurpSuite to capture a request to Easy-File-Share WebServer

i.e.
'''
GET / HTTP/1.1
Host: 172.16.0.24
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: SESSIONID=4219; UserID=; PassWD=
Upgrade-Insecure-Requests: 1
If-Modified-Since: Fri, 11 May 2012 10:11:48 GMT
Cache-Control: max-age=0
'''
2. Start constructing xml based off references below.....

i.e.

<Peach xmlns="http://peachfuzzer.com/2012/Peach" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://peachfuzzer.com/2012/Peach ../peach.xsd">

	<DataModel name="DataVfolder">
			<String value="GET /vfolder.ghp" mutable="false" token="true"/>					
			<String value=" HTTP/1.1" mutable="false" token="true"/>
			<String value="\r\n" mutable="false" token="true"/>

https://www.peach.tech/wp-content/uploads/HTTP.pdf

https://resources.infosecinstitute.com/fuzzing-vulnserver-with-peach-part-2/#gref

C:\peach.exe -h ##sounds dumb but 


## this is a large fuzz project but got many references to making xml work!


https://duo.com/blog/http2-peach-pit-for-microsoft-edge


https://github.com/sirusdv/EdgeHTTP2Fuzzer 


**PLUS the peachpro fuzz materials, I found from previous course. Will Include main docs used, but will provide complete package for any who I know.
