# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest

# Create your views here.
from django.http import HttpResponse

from django.http import Http404
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import serializers
from models import *

mongo_host = 'localhost'
mongo_port = 27017
mongo_endpoint = mongo_host + ":" + str(mongo_port)

def index(request):
    return HttpResponse("Hello, world. You're at the database index.")

@api_view(['POST'])
def insertData(request, table):
	if not request.data:
		return HttpResponseNotFound('Data is empty')

	data = request.data

	if table == "user":
		try:
			username = data['username']
			password = data['password']
			#print(id)
			age_range = data['age_range']
			#print(age_range)
			requirements = data['requirements']
			#print(requirements)
			job_years = data['job_years']
			#print(job_years)
			personality_color = data['personality_color']
			#print(personality_color)
			skills = data['skills']
			#print(skills)
			email = data['email']
			#print(contact)
			location = data['location']
			#print(location)
			name = data['name']
			#print(name)
			job_category = data['job_category']
			#print(job_category)
			education = data['education']
			#print(education)
			method = data['method']	
			#print(method)
			user_data = User_data(username=username, password=password, name=name, location=location, age_range=age_range, requirements=requirements, job_years=job_years, 
				personality_color=personality_color, email=email, education=education, method=method, skills=skills, job_category=job_category)
			user_data.save()
			#print("hahahaha")
		except KeyError as e:
			return HttpResponseBadRequest('Missing some of user data')
	elif table == "program":
		try:
			pid = data['pid']
			print(id)
			top_3_mentors = data['top_3_mentors']
			print(top_3_mentors)
			prog_stats = data['prog_stats']
			print(prog_stats)
			top_available_mentors = data['top_available_mentors']
			print(top_available_mentors)
			prog_data = Program(pid=pid, top_3_mentors=top_3_mentors, prog_stats=prog_stats, top_available_mentors=top_available_mentors)
			prog_data.save()
		except:
			return HttpResponseBadRequest('Missing some of program data')
	else:
		return HttpResponseBadRequest('Wrong table name')

	return HttpResponse("<h1>Saved!</h1>")
	
@api_view(['PUT'])
def updateData(request, table):
	data = request.data
	
	if table == "user":
		username = data['username']
		if not User_data.objects.filter(username=username).exists():
			return HttpResponseBadRequest('User record with username ' + username + ' does not exist')
		else:
			data.pop('username', None)
			user.objects.filter(username=username).update(**data)
			return HttpResponse('Put is successful')
	elif table == "program":
		pid = data['pid']
		if not Program.objects.filter(pid=pid).exists():
			return HttpResponseBadRequest('Program record with pid ' + str(pid) + ' does not exist')
		else:
			prog = Program.objects.get(pid=pid)
			data.pop('pid', None)
			Program.objects.filter(pid=pid).update(**data)
			return HttpResponse('Put is successful')
	else:
		return HttpResponseBadRequest('Put is not successful')

@api_view(['DELETE'])
def deleteData(request, table):
	data = request.data
	
	if table == "user":
		username = data['username']
		if not User_data.objects.filter(username=username).exists():
			return HttpResponseBadRequest('User record with username ' + username + ' does not exist')
		else:
			user = User_data.objects.get(username=username)
			user.delete()
	elif table == "program":
		pid = data['pid']
		if not Program.objects.filter(pid=pid).exists():
			return HttpResponseBadRequest('Program record with pid ' + str(pid) + ' does not exist')
		else:
			prog = Program.objects.get(pid=pid)
			prog.delete()
	else:
		return HttpResponseBadRequest('Wrong table name')
	
	return HttpResponse('Delete is successful')

@api_view(['GET'])
def parseRequest(request, table, id):
	data = request.data

	if table == 'user':
		username = data['username']
		try:
			data = User_data.objects.filter(username=username).values()
			print(data)
		except User_data.DoesNotExist:
			return HttpResponse(status=404)

		return HttpResponse(data)

	elif table == "program":
		pid = data['pid']
		try:
			data = Program.objects.filter(pid=id).values()
		except Program.DoesNotExist:
			return HttpResponse(status=404)
		return HttpResponse(data)
	else:
		return HttpResponseBadRequest('Wrong table name')
	