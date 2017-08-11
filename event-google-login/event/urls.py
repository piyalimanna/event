
from django.conf.urls import url, include
from django.contrib import admin
from ans.views import *
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^qs/(?P<number>\d)/$',question),
    url(r'^$',RedirectView.as_view(url='/qs/1/')),
    url(r'^accounts/', include('allauth.urls')),
    
]
