
from django.conf.urls import url
from ans.views import *

urlpatterns = [
    url(r'^register/$', register),
	url(r'^login/$', login),
	url(r'^logout/$',logoutView),
	url(r'^qs/(?P<number>\d)/$',question),
]
