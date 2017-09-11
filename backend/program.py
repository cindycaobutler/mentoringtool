from django.db import models
from djangotoolbox.fields import ListField, DictField, EmbeddedModelField

# Program model
class Program(models.Model):
    Top_3_mentors = ListField()
    Prog_stats = ListField()
    Top_Available_mentors  = ListField()
