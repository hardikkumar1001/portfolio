from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('defaultapp',
    # Examples:
    # url(r'^$', 'home_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'views.home'),
    #url(r'^admin/', include(admin.site.urls)),
)
