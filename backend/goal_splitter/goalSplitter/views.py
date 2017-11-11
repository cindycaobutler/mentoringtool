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
	temp = {"years":years1,"self_eva":self_eva1}
	goal1_list.append(temp)
	goal1_list.append(10)
	goal2_list=[]
	goal2_list.append(goal2)
	goal2_list.append(5)
	goal3_list=[]
	goal3_list.append(goal3)
	goal3_list.append(2)
	for line in datalist:
		if line.goal==goal1:
			temp = {"names":line.names,"years":line.years,"self_eva":line.self_eva}
			goal1_list.append(temp)
		if line.goal==goal2:
			temp = {"names":line.names,"years":line.years,"self_eva":line.self_eva}
			goal2_list.append(temp)
		if line.goal==goal3:
			temp = {"names":line.names,"years":line.years,"self_eva":line.self_eva}
			goal3_list.append(temp)
	#return HttpResponse("sdf")

# I just complete the algorithm of requirement calculator here, but I did not complete the django rest fran
def requirementCal(goal):
	mentee_data = goal[1]
	del goal[1]
	for i in range(2,len(goal)):
		year_gap = goal[i].years-mentee_data.years
		self_eva_diff = goal[i].self_eva - mentee_data.self_eva
		if year_gap>=3 and self_eva_diff - year_gap<=10:
			goal[i]={"name":goal[i].names,"score":year_gap+self_eva/2};
	return goal







