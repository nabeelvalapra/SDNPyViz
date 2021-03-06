from django.core.serializers import json
from django.http.response import HttpResponse
import requests
import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template import RequestContext
from django.shortcuts import render_to_response

# This needed to be shifted to settings.py
NODE_URL = '/controller/nb/v2/switchmanager/default/nodes'
NODE_INFO_URL = '/controller/nb/v2/switchmanager/default/node/'
PORT_URL = '/controller/nb/v2/statistics/default/port'
localhost = LOCALHOST = '192.168.1.9'
port = PORT = '8080'

NODE_URL = '/controller/nb/v2/switchmanager/default/nodes'
NODE_INFO_URL = '/controller/nb/v2/switchmanager/{containerName}/node/'
ODL_FLOWS = '/controller/nb/v2/flowprogrammer/default'

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
    response = {'nodes': get_switch(response)}
    return HttpResponse(json.dumps(response), content_type='application/json')

def get_flows(request):
    """
    return the json format for all the flows
    :param request:
    :return:
    """
    url = create_url('localhost', '8080', ODL_FLOWS)
    response = create_get_request(url, ('admin', 'admin'))

    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'flows': response['flowConfig']}
    return render_to_response('inventory/port.html',{'json':json.dumps(response)}, context_instance=RequestContext(request))


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('inventory/base.html', context_dict, context)

    return HttpResponse(json.dumps(response), content_type='application/json')
