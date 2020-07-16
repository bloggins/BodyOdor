#!/usr/bin/env python
from boofuzz import *


def main():

    f = open('easyfile-fuzz.csv', 'wb')

    start_cmd = ['C:\\EFS Software\\Easy File Sharing Web Server\\fsws.exe']
    target_ip = "172.16.0.24"
    session = Session(
        target=Target(
            connection=SocketConnection(target_ip,80,proto='tcp'),
            procmon=pedrpc.Client(target_ip,26002),
            procmon_options={"start_commands": [start_cmd]}
        ),
        sleep_time=1,
        fuzz_loggers=[FuzzLoggerText(),FuzzLoggerCsv(file_handle=f)]
        )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE'])
        s_delim(" ", name='space-1')
        s_string("/vfolder.ghp", name='Request-URI')
        s_delim(" ", name='space-2')
        s_string('HTTP/1.1', name='HTTP-Version')
        s_static("\r\n", name="Request-Line-CRLF")
    s_static("\r\n", "Request-CRLF")

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
    main()
