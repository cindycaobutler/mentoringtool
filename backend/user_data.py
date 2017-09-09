from django.db import models
from djangotoolbox.fields import ListField, DictField, EmbeddedModelField
import datetime

# USER_DATA model
class User_data(models.Model):
    name = models.CharField(max_length=64)
    location = models.TextField()
    contact = DictField()
    education = DictField()
    job_category = ListField()
    age_range = ListField()
    job_years = models.IntegerField(default='0')
    personality_color = models.CharField(max_length=64) # blue, red, green, yellow
    interest = models.CharField(max_length=256)
    programs = ListField()
    availability_mentor_per_week = models.IntegerField(default='0')
    num_of_mentees = models.IntegerField(default='0')
    num_of_mentors = models.IntegerField(default='0')
    reputation = models.IntegerField(default='0')
    updated_at = models.DateField(default=datetime.date.today)
    calendar = models.IntegerField(default='0')

    # Update job category
    def update_job_category(self, category):
        self.job_category = category
        self.updated_at = datetime.date.today()
        self.save()

    # Monthly mantaince
    def mantaince(self):
        if (datetime.date.today() - self.updated_at).days > 365:
            self.job_years += 1
            self.save()
