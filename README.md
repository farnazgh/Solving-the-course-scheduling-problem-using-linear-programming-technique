# Solving-the-course-scheduling-problem-using-linear-programming-technique

This program has two parts: the first part is for assigning timeslots to different courses and the second part is for assigning distinct classes to each course.

###course-scheduling-before:
assign timeslots to courses by LP technique

limitations:

1.Each course will be held in one timeslot only.

2.The number of classes that are held at a time slot must not be more than the number of vacant available classes at that time.

3.The lessons dedicated to any professor will be held at a time when the professor has a free time.

4.The lessons of a professor must be held at different time slots and the prof. can not have two or more lessons in a time slot.

object:

The number of classes is distributed uniformly at different time slots.

inputs:

Number of lessons - Number of classes - number of timeslots = number of professors - timeslots each professor is available - the courses are held by each professor in this semester


###course-scheduling-after:
assign classes to courses by LP technique

limitations:

1.Each lesson should be held in one class only.

2.Each class can only be assigned to one lesson within a given time slot.

3.The capacity of each class should be equal to or larger than the number of enrolled students in the course held in that class.

object: 

minimize the difference between class capacity and number of enrolled students (Do not assign a class with high capacity to a small group of students)

inputs:

class capacities - courses enrolments
