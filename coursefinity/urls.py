from django.conf.urls import patterns, url
from coursefinity import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^inspiration/$', views.inspiration, name='inspiration'),
	#ex coursefinity/onlinecareer/Developer/subjects :
	url(r'^onlinecareer/(?P<career_url>\w+)/(?P<program_url>\w+)/course_list$', views.course_list, name='course_list'),
	#ex coursefinity/onlinecareer/Developer :
	url(r'^onlinecareer/(?P<career_url>\w+)$', views.onlinecareer, name='onlinecareer'),
	url(r'^blog/$', views.blog, name='blog'),
	url(r'^contact/$', views.contact, name='contact'),
	)



