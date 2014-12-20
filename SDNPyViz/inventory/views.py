from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View
import requests
# Create your views here.

def getNodes(request):
    """
    this function retrieve the nodes.
    :return: json for the available node
    """

    return HttpResponse('this is working')