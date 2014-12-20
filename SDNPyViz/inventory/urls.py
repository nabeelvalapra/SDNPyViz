from django.conf.urls import patterns, url




urlpatterns = patterns('inventory.views',
    
    url(r'getNodes/$', 'getNodes', name='getNodes'),

)