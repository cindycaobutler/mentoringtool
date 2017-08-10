import pymongo

from pymongo import MongoClient

import datetime
import json


#db = client.test_database

#collection = db.test_collection

#post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

#posts = db.posts
#post_id = posts.insert_one(post).inserted_id
#post_id


class DB():

	def __init__(self):
		self.client = MongoClient('mongodb://localhost:27017/')
		self.db = self.client.mentor_tool
		self.user_table = self.db.user_table

	def insertPost(self, user_data):
		"""
		Input parameter: 
			user_data: string, must be key value pair JSON
		Outout parameter: void
			Insert JSON data into MongoDB

		Converts input string to dictionary and insert it to the table.
		"""

		print(user_data)
		data = json.loads(user_data);
		post_id = self.user_table.insert_one(data)

	def readPost(self, user_id, attr=None):
		"""
		Input parameter: 
			user_id: string
			attr: attributes want to query along with user_id, must be a key value pair JSON
		Output parameter: 
			data associate with user_id

		Read data from DB by primary key user_id, and with other attributes if exist. Return None if not exist.
		"""

		if not checkExist(user_id):
			return None

		query_filter = {'user_id': user_id}
		if attr:
			attr_json = json.loads(attr);
			for key, value in attr_json:
				query_filter[key] = value

		data = self.user_table.find_one(query_filter)

		return data

	def deletePost(self, user_id):
		"""
		Input parameter:
			user_id: string
		Output parameter: 
			void

		Remove a document from DB by user_id if user_id exist.
		"""
		if not checkExist(user_id):
			return

		query_filter = {'user_id': user_id}
		self.user_table.remove(query_filter)

	def checkExist(self, user_id):
		""" 
		Input parameter: 
			user_id: string
		Output parameter: 
			boolean indicates if the user_id info exist or not

		Check if the document exist in DB or not. Ture means exist, false means no.
		"""

		query_filter = {'user_id': user_id}
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

		if not checkExist(user_id):
			return False

		data = json.loads(user_data)
		input_data = {'user_id': user_id}
		for key, value in data:
			input_data[key] = value

		self.user_table.update_one(input_data)

		return True

if __name__ == "__main__":
	db = DB()
	user_id = 0
	name = "miaomiao"
	job_category = "SDE manager"
	years = 5
	skills = "Java, Python, AWS"
	requirements = "public speaking, leadership, music"
	method = 'online'
	self_assesment = '10, 10, 10'
	is_mentor = False
	programs = "[]"
	calendar = ""

	data = "{'user_id': %d, 'name': %s, 'job category': %s, 'years for current job category': %d, 'skills': %s, 'requirements': %s, 'method': %s, 'self assesment': %s, 'is mentor': %s, 'programs': %s, 'calendar': %s}" \
	% (user_id, name, job_category, years, skills, requirements, method, self_assesment, is_mentor, programs, calendar)
	db.insertPost(data)





