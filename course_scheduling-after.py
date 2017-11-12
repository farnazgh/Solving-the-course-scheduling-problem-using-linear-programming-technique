from __future__ import division
import pulp
import sys
import math

#get number of courses and classes
num_courses = int(raw_input("enter number of courses: "))
num_classes = int(raw_input("enter number of classes: "))
class_cap = [0 for i in range(num_classes)] 
course_cap = [0 for i in range(num_courses)] 

#get class capacities
print("class capacities: ")
for i in range(0, num_classes):
	_input = raw_input() 
	
	class_index = int(_input.split(' ', 1 )[0])-1
	class_capacity = int(_input.split(' ', 1 )[1])
	class_cap[class_index] =  class_capacity
	
#get course enrollments
print("course enrollments: ")
for i in range(0, num_courses):
	_input = raw_input() 
	
	course_index = int(_input.split(' ', 1 )[0])-1
	course_enrollments = int(_input.split(' ', 1 )[1])
	course_cap[course_index] =  course_enrollments

#Creates an LP Problem
lp_prob = pulp.LpProblem("course scheduling Problem", pulp.LpMinimize)


#Define variables
x = [[0 for i in range(num_courses)] for j in range(num_classes)] 

for i in range(0, num_courses):
	for j in range(0, num_classes):
		x[i][j] = pulp.LpVariable("x_"+str(i)+"_"+str(j), lowBound=0, upBound=1, cat='Binary')


#Define Object
sum_object = 0;
for i in range(0, num_courses):
	for j in range(0, num_classes):
		c_ij = class_cap[j] / course_cap[i]
		sum_object += c_ij*x[i][j]*100
lp_prob += sum_object


#Define constraints
#condition 1
for i in range(0, num_courses):
	sum_xi=0
	for j in range(0, num_classes):
		sum_xi+= x[i][j]
	lp_prob += sum_xi ==1
#condition 2
for j in range(0, num_classes):
	sum_xj=0
	for i in range(0, num_courses):
		sum_xj+= x[i][j]
	lp_prob += sum_xj <=1

#condition 3
sum_T=0;
for i in range(0, num_courses):
	for j in range(0, num_classes):
		if(course_cap[i]>class_cap[j]):
			sum_T += x[i][j]
lp_prob += sum_T ==0


#solve problem
lp_prob.solve()


#print resutls
for v in lp_prob.variables():
    print(v.name, "=", v.varValue)
print("Total Cost =", math.ceil(pulp.value(lp_prob.objective)))
