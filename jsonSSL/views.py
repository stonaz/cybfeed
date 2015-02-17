import json
import socket, ssl
from django.shortcuts import render
from django.http import HttpResponse
from utils import jsonSSL_socket 



def index(request):
    jsonSSL = (request.body)
    socket_request = jsonSSL
    try:
        socket_response = jsonSSL_socket(socket_request)
    except ssl.SSLError as err:
        return HttpResponse(err)
    return HttpResponse(socket_response)
