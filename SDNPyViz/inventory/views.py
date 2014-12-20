from django.http.response import HttpResponse
import requests
import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext
# Create your views here.

NODE_URL = '/controller/nb/v2/switchmanager/default/nodes'
NODE_INFO_URL = '/controller/nb/v2/switchmanager/default/node/'
PORT_URL = '/controller/nb/v2/statistics/default/port'
localhost = LOCALHOST = '192.168.1.9'
port = PORT = '8080'

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
        return r.json()

def get_nodes(request):
    """
    this function retrieve the nodes.
    :return: json for the available node
    """
    url = create_url('192.168.1.9', '8080', NODE_URL)
    response = create_get_request(url, ('admin', 'admin'))
    return HttpResponse(response, content_type='json')


def port_info(request):
    """
    this function retrieve the port.
    :return: json for the ports
    """
    url = create_url(localhost, port, PORT_URL)
    response = create_get_request(url, ('admin','admin'))
    return render_to_response('inventory/port.html',{}, context_instance=RequestContext(request))
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4), content_type='json')


