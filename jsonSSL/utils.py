import os
import socket, ssl, pprint
import subprocess

from django.conf import settings

SERVICES = {
'node': {
'name': ('Node insertion'),
'description': ('Insert new nodes'),
'keywords': '',
'group': ''
},
}

def jsonSSL_socket(json_request):
    CERTS_DIR = os.path.dirname(__file__) + '/certs/'
    CERTS_DIR = '/home/stefano/python-progs/certs/'
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(s,
                           ca_certs = CERTS_DIR + "ca.pem",
                           certfile = CERTS_DIR + "client.pem",
                           keyfile = CERTS_DIR + "client.key",
                           cert_reqs = ssl.CERT_REQUIRED,
                           ssl_version = ssl.PROTOCOL_TLSv1,
                           )
                         
    ssl_sock.connect(('127.0.0.1',5151))
    ssl_sock.send(json_request)
    print repr(ssl_sock.getpeername())
    print ssl_sock.cipher()
    print pprint.pformat(ssl_sock.getpeercert())
    socket_response = ssl_sock.recv(4096)
    return(socket_response)
    ssl_sock.close()
    
def update_DNSD_config():
    start_marker = "#CyberFeedBegin\n" #Simply #CyberFeedBegin in dnsd.conf
    end_marker = "#CyberFeedEnd\n" #Simply #CyberFeedEnd in dnsd.conf
    FLAGFILE="/home/stefano/python-progs/CyberFeed/feed.conf"
    DNSDCONFIGFILE="/home/stefano/python-progs/CyberFeed/dnsd.conf"
    DNSDBACKUPFILE="/home/stefano/python-progs/CyberFeed/dnsd-bak.conf"
    UPDATECONFIGFILE="/home/stefano/python-progs/CyberFeed/update-dnsd.py"
    dim = []
    # Stores contents of the feed in a list
    feed = open(FLAGFILE, 'r')
    feedlines = feed.readlines()
    feed.close()
    
    # Stores contents of the dnsd config file in a list
    f = open(DNSDCONFIGFILE, 'r')
    lines = f.readlines()
    f.close()
    
    # Creates a new dnsd config file replacing the content between the markers
    # with the content of the feed file
    f = open(DNSDCONFIGFILE, 'w')
    write = True
    for line in lines:
        if line == start_marker:
            f.write(line)
            write = False
            #print 'matched'
            for feedline in feedlines:
                f.write(feedline)
            f.write('\n')
        if line == end_marker:
            write = True
        if write:
            f.write(line)
    f.close()
    p = subprocess.Popen(["ping", "-c", "3", "www.cyberciti.biz"], stdout=subprocess.PIPE)
    #output, err = p.communicate()
    for line in iter(p.stdout.readline, ''):
        dim.append(line.rstrip('\n'))
        print dim
    return(dim)