import json
import socket, ssl
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from utils import jsonSSL_socket 



def index(request):
    jsonSSL = (request.body)
    socket_request = jsonSSL
    try:
        socket_response = jsonSSL_socket(socket_request)
    except ssl.SSLError as err:
        socket_response={ err}
        return HttpResponse(socket_response)
    return HttpResponse(socket_response)

class SocketApi(generics.ListCreateAPIView):
    """
    make request to socket
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )
    def post(self,request):
        print request.user
        print request.body
        socket_request = request.body
        try:
            socket_response = jsonSSL_socket(socket_request)
        except ssl.SSLError as err:
            print type(err)
            #print json.dump(err,test)
            print err.__unicode__()
            #content = {'Error': json.dumps(err)}
            #err_json = json.JSONEncoder(err)
            #print json.loads(err_json)
            content = {'Error': err.__unicode__()}

            #socket_response={ err}
            return Response(content, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            #return Response(socket_response)
        return Response(socket_response)

socket_api = SocketApi.as_view()
