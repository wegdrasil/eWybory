from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Poll.views.home', name='home'),
    url(r'^vote/$', 'Poll.views.thankyou', name='thankyou'),
    url(r'^vote/(?P<Poll_id>\d+)/result/$', 'Poll.views.result', name='result'),
    url(r'^register/$', 'Poll.views.register', name='register'),
    url(r'^login/$', 'Poll.views.user_login', name='user_login'),
    url(r'^logout/$', 'Poll.views.user_logout', name='user_logout'),
    url(r'^(?P<Poll_id>\d+)/vote/$', 'Poll.views.voting', name='voting'),
    # url(r'^voting/$', 'Poll.views.voting', name='voting'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)