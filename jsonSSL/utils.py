import os
import socket, ssl, pprint

from django.conf import settings

def jsonSSL_socket(json_request):
    CERTS_DIR = os.path.dirname(__file__) + '/certs/'
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(s,
                           ca_certs= CERTS_DIR + "root.crt",
                           certfile = CERTS_DIR + "client.crt",
                           keyfile = CERTS_DIR + "client.key",
                           cert_reqs=ssl.CERT_REQUIRED,
                           ssl_version=ssl.PROTOCOL_TLSv1,
                           )
                         
    ssl_sock.connect(('127.0.0.1',5151))
    ssl_sock.send(json_request)
    print repr(ssl_sock.getpeername())
    print ssl_sock.cipher()
    print pprint.pformat(ssl_sock.getpeercert())
    socket_response = ssl_sock.recv(4096)
    return(socket_response)
    ssl_sock.close()