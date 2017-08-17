import pymongo

from pymongo import MongoClient

import datetime
import json


class DB():
	'''
	USERS_DATA schema:
	_id = unique value
	name = "string"
	location = "string"
	education = {json object with major, degree, and school }
	job category = array of json objects
					[{SW: {
					  SW1: 1, 
					  SW2: 0, 
					  SW3: 0 
					}},
					 {PM:{
					  PM1:,
					  PM2:,
					  PM3:
					}},
					 {Mkt
					]
					age_range  = [array eg values 20-30 etc ]
					years of job_category = integer 
					personality color = [array with blue, red, green ,yellow ]
					Interests = string
					skills = json object
					requirements = "string"
					method = "string"
					programs = array of json objects
					[{
					 P1: 
				
					},
					{
					 P2:
					}
					]
	is_mentor = boolean

	'''

	def __init__(self):
		self.client = MongoClient('mongodb://localhost:27017/')
		self.db = self.client.mentor_tool
		self.user_table = self.db.USERS_DATA

	def insertPost(self, user_data):
		"""
		Input parameter: 
			user_data: string, must be key value pair JSON
		Outout parameter: void
			Insert JSON data into MongoDB

		Converts input string to dictionary and insert it to the table.

		user data format:
		

		"""

		#print(user_data)
		#data = user_data.split(';')
		#doc = {}
		#education = data[3].split(',')
		#job_category = data[4].split('')
		#edu = {'major': education[0], 'degree': education[1], 'school': education[2]}
		#doc['_id'] = data[0]
		#doc['name'] = data[1]
		#doc['location'] = data[2]
		#doc['education'] = edu
		#doc['job category']= {}

		data = json.loads(user_data);
		res = True
		try:
			post_id = self.user_table.insert_one(data)
		except:
			print("Duplicate key, insertion failed!")
			res = False
		finally:
			if res:
				print("Insertion success")
			return

	def readPost(self, user_id, attr=None):
		"""
		Input parameter: 
			user_id: int
			attr: attributes want to query along with user_id, must be a key value pair JSON
		Output parameter: 
			data associate with user_id

		Read data from DB by primary key user_id, and with other attributes if exist. Return None if not exist.
		"""

		if not self.checkExist(user_id):
			return None

		query_filter = {'_id': user_id}
		if attr:
			attr_json = json.loads(attr);
			for key, value in attr_json:
				query_filter[key] = value

		data = self.user_table.find_one(query_filter)

		return data

	def deletePost(self, user_id):
		"""
		Input parameter:
			user_id: int
		Output parameter: 
			void

		Remove a document from DB by user_id if user_id exist.
		"""
		if not self.checkExist(user_id):
			return False

		query_filter = {'_id': user_id}
		self.user_table.remove(query_filter)
		return True

	def checkExist(self, user_id):
		""" 
		Input parameter: 
			user_id: int
		Output parameter: 
			boolean indicates if the user_id info exist or not

		Check if the document exist in DB or not. Ture means exist, false means no.
		"""

		query_filter = {'_id': user_id}
		cnt = self.user_table.find(query_filter).count()
		if (cnt > 0):
			return True

		return False

	def update(self, user_id, user_data):
		"""
		Input parameter:
		user_id: string
		data: string, must be a kay value pair JSON
		Output parameter:
		boolean indicates if update is successful or not
		"""

		if not self.checkExist(user_id):
			return False

		query_filter = {}
		query_filter['_id'] = user_id
		input_data = {'$set': json.loads(user_data)}

		print(input_data)
		#data = json.loads(user_data)
		#data['_id'] = user_id
		#print(data)
		#for key, value in data:
		#	input_data[key] = value

		self.user_table.update(query_filter, input_data)

		return True

if __name__ == "__main__":
	db = DB()
	user_id = 0
	name = "miaomiao"
	job_category = [{'SW': {'SW1': 1, 'SW2': 0, 'SW3': 0 }},{'PM':{'PM1': 0,'PM2': 2,'PM3': 0}}]
	education = {'major': 'EE', 'degree':'MS', 'school':'University of Michigan'}
	years_of_job_category = 5 
	personality_color = ['red', 'blue']
	Interests = "Music, Gaming"
	age_range = "20-30"
	skills = {'Java': 10, 'Python': 10, 'AWS': 10}
	requirements = "public speaking, leadership, music"
	method = 'online'
	is_mentor = False
	programs = [{}]
	calendar = ""

	#data = "{'id': %d, 'name': %s, 'job category': %s, 'years for current job category': %d, 'skills': %s, 'requirements': %s, 'method': %s, 'self assesment': %s, 'is mentor': %s, 'programs': %s, 'calendar': %s}" \
	#% (user_id, name, job_category, years, skills, requirements, method, self_assesment, is_mentor, programs, calendar)
	data = {}
	data['_id'] = user_id
	data['name'] = name
	data['job_category'] = job_category
	data['education'] = education
	data['years_of_job_category'] = 5
	data['personality_color'] = personality_color
	data['Interests'] = Interests
	data['age_range'] = age_range
	data['skills'] = skills
	data['requirements'] = requirements
	data['method'] = method
	data['is_mentor'] = is_mentor
	data['programs'] = programs

	db.insertPost(json.dumps(data))

	read_data = db.readPost(0)
	if read_data is None:
		print("data is none")
	else:
		print(read_data)

	#if db.deletePost(0):
	#	print("delete is successful")
	#else:
	#	print("hehe")

	update_data = {}
	update_data['job_category'] = job_category
	programs = [{'prog': 'music', 'mentor': False, 'partener': 'YuanMiao'}]
	update_data['programs'] = programs
	if db.update(0, json.dumps(update_data)):
		print("update is successful")
	else:
		print("Hehe")







