from django.db import models
from djangotoolbox.fields import ListField, DictField, EmbeddedModelField
import datetime

class Prog(models.Model):
    '''
    programs = array of json objects
    [   Prog1:{
        Pid: unique 
        Buddy_name = String
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
    '''
    prog = DictField()

# USER_DATA model
class User_data(models.Model):
    '''
    USERS_DATA schema:
    _id = unique value
    name = "string"
    location = "string"
    education = {json object with major, degree, and school }
    job category = array of json objects
                    [{SW: {
                      SW1: < 3 year3
                      SW2: < 1 year 
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
    [   Prog1:{
        Pid: unique 
        Buddy_name = String
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
    Example:
    {
        "name": "miao", 
        "age_range": "30-45",
        "requirements": "public speaking;english;software",
        "job_years": 3,
        "skills": {
            "Java":10, 
            "Python":10},
        "contact": {
            "Phone": "1234567890", 
            "email": "abc@def.com"
        },
        "personality_color": [0.4, 0.3, 0.2, 0.1],
        "job_category": [{
            "SW1": 2, 
            "SW2":1
        }, 
            {
                "PM1":1
            }],
        "education": {
            "Highest degree": "PHD", 
            "Major":"play", 
            "School":"University of jialidun", 
            "Year of graduation": 3975
        }, 
        "id": 0,
        "location": "jiali",
        "method": "online"
    }
    '''
    username = models.TextField() # username
    password = models.TextField()
    name = models.CharField(max_length=64)
    location = models.TextField()
    email = DictField() # email
    education = DictField()
    job_category = ListField()
    #age_range = ListField()
    age_range = models.CharField(max_length=64)
    job_years = models.IntegerField(default='0')
    #personality_color = models.CharField(max_length=64) # blue, red, green, yellow
    personality_color = ListField() # blue, red, green, yellow
    interest = models.CharField(max_length=256)
    skills = DictField()
    requirements = models.TextField()
    method = models.CharField(max_length=64)
    programs = ListField()
    ######## ??? #########
    availability_mentor_per_week = models.IntegerField(default='0')
    num_of_mentees = models.IntegerField(default='0')
    num_of_mentors = models.IntegerField(default='0')
    reputation = models.IntegerField(default='0')
    updated_at = models.DateField(default=datetime.date.today)
    calendar = models.TextField()

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

    def exists(self, user_name): 
        return User_data.objects.filter(username=user_name).exists()
    # Update user info
    # def update_user_info(self, id, name, location, contact, education, age_range, job_years):