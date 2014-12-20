from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View
import requests
# Create your views here.

NODE_URL = '/controller/nb/v2/switchmanager/default/nodes'
NODE_INFO_URL = '/controller/nb/v2/switchmanager/{containerName}/node/'

def create_url(ip, port, url):
    """
    this function creates the url.
    :param ip:
    :param port:
    :param url:
    :return:
    """
    return 'http://' + ip + ':' + port + url

def create_get_request(url, credential):
    """
    this function create the get request and return the json response.
    :param url:
    :param credential:
    :return:
    """
    r = requests.get(url, auth=credential)

    if r.status_code == 200:
        return r.content


def get_nodes(request):
    """
    this function retrieve the nodes.
    :return: json for the available node
    """
    url = create_url('localhost', '8080', NODE_URL)
    response = create_get_request(url, ('admin', 'admin'))
    return HttpResponse(response, content_type='json')