from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from sweet_dating import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sweet_dating.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'sweet_dating_app.views.home', name='home'),
    url(r'^add_portfolio/$', 'sweet_dating_app.views.add_portfolio', name='add_portfolio'),

    url(r'^profile/$', 'sweet_dating_app.views.profile', name='profile'),
    url(r'^faq/$', 'sweet_dating_app.views.faq', name='faq'),
    url(r'^register/$', 'sweet_dating_app.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)