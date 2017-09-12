from django.db import models
from djangotoolbox.fields import ListField, DictField, EmbeddedModelField
import datetime

# Program model
class Program(models.Model):
	'''
	PROGRAMS schema:
	_id = unique 
	Top_3_mentors = array of json object with name: 'string' and _id: integer
	Prog_stats = json object with no_of_users: integer and no_of_users_this_month:integer 
	Top_Available_mentors = array of json object with name: 'string' and _id: integer

	'''
	pid = models.IntegerField(default='0', primary_key=True)
	top_3_mentors = ListField()
	prog_stats = DictField()
	top_available_mentors  = ListField()

	updated_at = models.DateField(default=datetime.date.today)

	def update_top_3_mentors(self, id, mentors):
		if (Program.objects.filter(pid=id).exists()):
			print("Updating entry")
			no_entry = self.objects.filter(pid=id).update(top_3_mentors=mentors)
			self.save()
			return True
		else:
			print("Entry IS NOT contained in queryset")
			return False

	def update_top_available_mentors(self, id, top):
		if (Program.objects.filter(pid=id).exists()):
			print("Updating entry")
			no_entry = self.objects.filter(pid=id).update(top_available_mentors=top)
			self.save()
			return True
		else:
			print("Entry IS NOT contained in queryset")
			return False

	def exists(self, id):
		if Program.objects.filter(pid=id).exists():
			return True
		return False
	
	def update_prog_stats(self, id, no_of_users):
		if (Program.objects.filter(pid=id).exists()):
			print("Updating entry")
			prog = Program.objects.filter(pid=id).first()
			prog.prog_stats["no_of_users"] += no_of_users
			tmp = prog.prog_stats["no_of_users_this_month"]
			if datetime.date.today() - self.updated_at.days > 30:
				prog.prog_stats["no_of_users_this_month"] = no_of_users
			else:
				prog.prog_stats["no_of_users_this_month"] += no_of_users

			updated_at = models.DateField(default=datetime.date.today)
			self.save()
			return True
		else:
			print("Entry IS NOT contained in queryset")
			return False

	def mantaince(self):
		if datetime.date.today() - self.updated_at.days > 30:
			self.prog_stats["no_of_users_this_month"] = 0



# class ProgStat(models.Model):
# 	'''
# 	no_of_users: integer
# 	no_of_users_this_month: integer
# 	'''

# 	no_of_users = models.IntegerField(default='0')
# 	no_of_users_this_month = models.IntegerField(default='0')

# class Mentors(models.Model):
# 	'''
# 	Mentor name and id
# 	'''

# 	name = models.CharField(max_length=64)
# 	mid = models.IntegerField(default='0')