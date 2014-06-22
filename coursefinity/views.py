from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from coursefinity.models import Link, Career, Program, Courses

def encode_url(str):
	return str.replace(' ', '_')

def decode_url(str):
	return str.replace('_', ' ')

def get_career_list():
	career_list = Career.objects.all()

	for career in career_list:
		career.url = encode_url(career.name)
	return career_list


def get_program_list():

	program_list = Program.objects.all()

	for prog in program_list:
		prog.url = encode_url(prog.name)
	
	return program_list


def index(request):

	context = RequestContext(request)

	career_list = get_career_list()

	context_dict = {'career_list': career_list}

	return render_to_response('coursefinity/index.html', context_dict, context)

def onlinecareer(request, career_url): 
#kanina hindi madetect ung career_url unnecessary argument daw, ngayon ok na
#walang pinass na argument dito
	context = RequestContext(request)

	program_list = get_program_list()

	context_dict = {'program_list': program_list}

	career = Career.objects.get(name=career_url) #ah para pala to sa career.name

	context_dict['career'] = career 

	return render_to_response('coursefinity/onlinecareer.html', context_dict, context)

def course_list(request, career_url, program_url):

	context = RequestContext(request)

	course_list = Courses.objects.all()
	
	program_list = get_program_list()

	context_dict = {'program_list': program_list, 'course_list': course_list}

	return render_to_response('coursefinity/course_list.html', context_dict, context)




def blog(request):
	return render(request, 'coursefinity/blog.html')

def contact(request):
	return render(request, 'coursefinity/contact.html')

def inspiration(request):
	#obtain context from the Http request
	context = RequestContext(request)

	article_list = Link.objects.all()
	context_dict = {'article_list': article_list}

	return render_to_response('coursefinity/inspiration.html', context_dict, context)



