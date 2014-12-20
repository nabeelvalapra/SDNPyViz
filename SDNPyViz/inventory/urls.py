from django.conf.urls import patterns, url




urlpatterns = patterns('inventory.views',
    
    url(r'getNodes/$', 'get_nodes', name='get_nodes'),

)