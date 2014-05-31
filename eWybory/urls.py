from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Poll.views.home', name='home'),
    url(r'^thank-you/$', 'Poll.views.thankyou', name='thankyou'),
    url(r'^result/$', 'Poll.views.result', name='result'),
    url(r'^register/$', 'Poll.views.register', name='register'),
    url(r'^login/$', 'Poll.views.user_login', name='user_login'),
    url(r'^logout/$', 'Poll.views.user_logout', name='user_logout'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)