from django.core.serializers import json
from django.http.response import HttpResponse
import requests
import json
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
        return r.json()

def get_switch(json_data):
    """
    this function return the array of the switch
    :param json_data:
    :return:
    """
    return [node['node']['id'] for node in json_data['nodeProperties'] or []]

def get_nodes(request):
    """
    this function retrieve the nodes.
    :return: json for the available node
    """
    url = create_url('localhost', '8080', NODE_URL)
    response = create_get_request(url, ('admin', 'admin'))

    response = {'nodes': get_switch(response)}
    return HttpResponse(json.dumps(response), content_type='json')