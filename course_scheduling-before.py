from __future__ import division
import pulp
import sys
import math
#!/usr/bin/python

#get number of courses and classes
num_courses = int(raw_input("enter number of courses: "))
num_classes = int(raw_input("enter number of classes: "))
class_cap = [0 for i in range(num_classes)] 
course_cap = [0 for i in range(num_courses)] 

num_timeslots = int(raw_input("enter number of time slots: "))
num_prof = int(raw_input("enter number of professors: "))

prof_tslot = [[0 for i in range(num_timeslots)] for j in range(num_prof)] 
prof_course = [[0 for i in range(num_courses)] for j in range(num_prof)] 

for i in range(0, num_prof):
	for j in range(0, num_timeslots):
		prof_tslot[i][j] =  0

for i in range(0, num_prof):
	for j in range(0, num_courses):
		prof_course[i][j] =  0


#get each prof tslot
print("enter professors feasible time slots: ")
while(True):
	_input = raw_input() 
	
	if(_input=="END"): break

	prof = int(_input.split(' ', 1 )[0])-1
	tslot = int(_input.split(' ', 1 )[1])-1
	prof_tslot[prof][tslot] =  1


	
#get each prof courses
print("enter professors' courses: ")
for i in range(0, num_courses):
	_input = raw_input() 
	
	prof = int(_input.split(' ', 1 )[0])-1
	course = int(_input.split(' ', 1 )[1])-1
	prof_course[prof][course] =  1

#Creates an LP Problem
lp_prob = pulp.LpProblem("course scheduling Problem", pulp.LpMinimize)


#Define variables
x = [[0 for i in range(num_timeslots)] for j in range(num_courses)] 

for i in range(0, num_courses):
	for j in range(0, num_timeslots):
		x[i][j] = pulp.LpVariable("x_"+str(i)+"_"+str(j), lowBound=0, upBound=1, cat='Binary')


#Define Object
mean = (num_courses/num_timeslots)
var=0
for i in range(0, num_timeslots):
	sum_courses =0;
	for j in range(0, num_courses):
		sum_courses += x[j][i];
	
	var += (sum_courses - mean)
lp_prob += var


#Define constraints
#condition 1
for i in range(0, num_courses):
	sum_xi=0
	for j in range(0, num_timeslots):
		sum_xi += x[i][j]
	lp_prob += sum_xi ==1

#condition 2
for j in range(0, num_timeslots):
	sum_xj=0
	for i in range(0, num_courses):
		sum_xj+= x[i][j]
	lp_prob += sum_xj <=num_classes

#condition 3
for i in range(0, num_courses):
	for j in range(0, num_prof):
		if(prof_course[j][i]==1):
			for k in range(0, num_timeslots):
				if(prof_tslot[j][k]==0):
					lp_prob += x[i][k] ==0


#conditoin 4
for i in range(0, num_prof):
	for j in range(0, num_timeslots):
		if(prof_tslot[i][j]==1):

			sum_courses=0
			for k in range(0, num_courses):
				if(prof_course[i][k]==1):
					sum_courses += x[k][j]

			lp_prob += sum_courses<=1

#solve problem
lp_prob.solve()


#print resutls
for v in lp_prob.variables():
    print(v.name, "=", v.varValue)
print("Total Cost =", math.ceil(pulp.value(lp_prob.objective)))
