from django.conf.urls import patterns, include, url
from django.contrib import admin
import main.views as v

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',v.index),
    url(r'^imguruploader$',v.imguruploader),
    url(r'^info$', v.apidetails,),
    url(r'^uid$', v.apiuid,),
)
