from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
	if request.method == "POST":
		goal1 = request.POST.get("goal1",None)
		goal2 = request.POST.get("goal2",None)
		goal3 = request.POST.get("goal3",None)
	#get the data from the database, each row include: goal name, years & self-eva
	goal1_list=[]
	goal1_list.append(goal1)
	goal1_list.append(10)
	goal2_list=[]
	goal2_list.append(goal2)
	goal2_list.append(5)
	goal3_list=[]
	goal3_list.append(goal3)
	goal3_list.append(2)
	for line in datalist:
		if line.goal==goal1:
			temp = {"years":line.years,"self_eva":line.self_eva}
			goal1_list.append(temp)
		if line.goal==goal2:
			temp = {"years":line.years,"self_eva":line.self_eva}
			goal2_list.append(temp)
		if line.goal==goal3:
			temp = {"years":line.years,"self_eva":line.self_eva}
			goal3_list.append(temp)
	#return HttpResponse("sdf")
