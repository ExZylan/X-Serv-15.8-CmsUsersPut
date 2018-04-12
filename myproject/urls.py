from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout, login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cms.views.barra'),
    url(r'^page/(\d+)$', 'cms.views.pages'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout', logout),
    url(r'^login', login),
)
