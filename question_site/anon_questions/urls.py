from django.conf.urls import patterns, include, url

urlpatterns = patterns('anon_questions.views',
    # Examples:
    # url(r'^$', 'firstsite.views.home', name='home'),
    # url(r'^firstsite/', include('firstsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'index'),
    url(r'^ask/$', 'ask'),
    url(r'^(?P<question_id>\d+)/$', 'detail'),
    url(r'^(?P<question_id>\d+)/answer/$', 'answer'),
)
