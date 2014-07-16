from django.conf.urls import patterns, include, url

from coursefinity import views#

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coursefinityProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include('coursefinity.urls')),
    url(r'^$', views.index, name='index'),
	url(r'^coursetracks/$', views.coursetracks, name='coursetracks'),
	url(r'^inspiration/$', views.inspiration, name='inspiration'),
	#ex coursefinity/coursetracks/Developer/subjects :
	url(r'^coursetracks/(?P<career_url>\w+)/(?P<program_url>\w+)/course_list$', views.course_list, name='course_list'),
	#ex coursefinity/coursetracks/Developer :
	url(r'^coursetracks/(?P<career_url>\w+)$', views.onlinecareer, name='onlinecareer'),
	url(r'^about/$', views.about, name='about'),
)
