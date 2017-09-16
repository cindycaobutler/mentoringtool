import pymongo

from pymongo import MongoClient

import datetime
import json
from mongoengine import *
connect('mentor_tool')

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
	years_of_job_category = integer 
	personality color = [array with blue, red, green ,yellow ]
	Interests = string
	skills = json object
	requirements = "string"
	method = "string"
	programs = array of json objects
	[	Prog1:{
		Pid: unique 
		Buddy_name = {json objects with mentor = 'String', mentee= 'String'}
		As mentor: boolean 
		ranking as mentor: integer range 1-10
		Skill self eval: integer range 1-10 
		Start date:''
		End date:''
		is _Online: boolean
		is_in_person : boolean
		Score : integer 
		}
	Prog2:{

	}]
	is_mentor = boolean
	availability_as_mentor_per_week = integer 
	num_of_mentees =  integers
	num_of_mentors =  integers
	Reputation = integer

	'''

	'''
	PROGRAMS schema:
	_id = unique 
	Top_3_mentors = array of json object with name: 'string' and _id: integer
	Prog_stats = array of json object with no_of_users: integer and no_of_users_this_month:integer 
	Top_Available_mentors = array of json object with name: 'string' and _id: integer

	'''

	def __init__(self):
		self.client = MongoClient('mongodb://localhost:27017/')
		self.db = self.client.mentor_tool
		self.user_table = self.db.USERS_DATA
		self.prog_table = self.db.PROGRAMS



	def insertPost(self, table, data):
		"""
		Input parameter: 
			user_data: string, must be key value pair JSON
			table: table to insert user data, should be either "program" or "user"
		Outout parameter: void
			Insert JSON data into MongoDB

		Converts input string to dictionary and insert it to the table.

		user data format:
		

		"""
		#print(data['id'])
		#print(self.checkExist(table, data['id']))
		if self.checkExist(table, data['id']) or not self.validateTable(table):
			print("hehe")
			return False
		else:
			print("????????")
		res = True
		try:
			if table == 'user':
				post_id = self.user_table.insert_one(data)
			else:
				post_id = self.prog_table.insert_one(data)
		except:
			print("Duplicate key, insertion failed!")
			res = False
		finally:
			print("Write status " + str(post_id.acknowledged))
			#print("Post id " + str(post_id.insertedId))
			if res:
				print("Insertion success")
			return res

	def readPost(self, table, id, attr=None):
		"""
		Input parameter: 
			table: table to insert user data, should be either "program" or "user"
			id: int
			attr: attributes want to query along with id, must be a key value pair JSON
		Output parameter: 
			data associate with id

		Read data from DB by primary key id, and with other attributes if exist. Return None if not exist.
		"""

		if not self.checkExist(table, id) or not self.validateTable(table):
			return None

		query_filter = {'_id': id}
		if attr:
			attr_json = json.loads(attr);
			for key, value in attr_json:
				query_filter[key] = value

		data = {}
		if table == 'user':
			data = self.user_table.find_one(query_filter)
		else:
			data = self.prog_table.find_one(query_filter)

		return data

	def deletePost(self, table, id):
		"""
		Input parameter:
			table: table to insert user data, should be either "program" or "user"
			id: int
		Output parameter: 
			boolean indicate is delete post is successful

		Remove a document from DB by id if id exist.
		"""
		if not self.checkExist(table, id) or not self.validateTable(table):
			return False

		query_filter = {'_id': id}
		if table == 'user': 
			self.user_table.remove(query_filter)
		else:
			self.prog_table.remove(query_filter)
		return True

	def checkExist(self, table, id):
		""" 
		Input parameter: 
			table: table to insert user data, should be either "program" or "user"
			id: int
		Output parameter: 
			boolean indicates if the id info exist or not

		Check if the document exist in DB or not. Ture means exist, false means no.
		"""

		query_filter = {'_id': id}
		cnt = 0
		if table == 'user':
			cnt = self.user_table.find(query_filter).count()
		else:
			cnt = self.prog_table.find(query_filter).count()
		print(cnt)
		if (cnt > 0):
			return True

		return False

	def validateTable(self, table):
		
		return (table == 'user') or (table == 'program')

	def update(self, table, id, user_data):
		"""
		Input parameter:
			table: table to insert user data, should be either "program" or "user"
			id: integer
			data: string, must be a kay value pair JSON
		Output parameter:
			boolean indicates if update is successful or not
		"""

		if not self.checkExist(table, id) or not self.validateTable(table):
			return False

		query_filter = {}
		query_filter['_id'] = id

		input_data = {'$set': user_data}

		if table == 'user':
			self.user_table.update(query_filter, input_data)
		else:
			self.prog_table.update(query_filter, input_data)

		return True

if __name__ == "__main__":
	db = DB()
	id = 0
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
	#% (id, name, job_category, years, skills, requirements, method, self_assesment, is_mentor, programs, calendar)
	data = {}
	data['_id'] = id
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

	db.insertPost('user', data)

	read_data = db.readPost('user', 0)
	if read_data is None:
		print("data is none")
	else:
		print(read_data)

	if db.deletePost('user', 0):
		print("delete is successful")
	else:
		print("hehe")

	update_data = {}
	update_data['job_category'] = job_category
	programs = [{'prog': 'music', 'mentor': False, 'partener': 'YuanMiao'}]
	update_data['programs'] = programs
	if db.update(0, 'user', update_data):
		print("update is successful")
	else:
		print("Hehe")







