from django.conf.urls import patterns, url
from coursefinity import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^coursetracks/$', views.coursetracks, name='coursetracks'),
	url(r'^inspiration/$', views.inspiration, name='inspiration'),
	#ex coursefinity/coursetracks/Developer/subjects :
	url(r'^coursetracks/(?P<career_url>\w+)/(?P<program_url>\w+)/course_list$', views.course_list, name='course_list'),
	#ex coursefinity/coursetracks/Developer :
	url(r'^coursetracks/(?P<career_url>\w+)$', views.onlinecareer, name='onlinecareer'),
	url(r'^blog/$', views.blog, name='blog'),
	url(r'^about/$', views.about, name='about'),
	)



