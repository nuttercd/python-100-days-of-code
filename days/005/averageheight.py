#This challenge does not allow you the use of len() or sum()
#Heights: 156 178 165 171 187
#

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#sum() using a for loop
total_height = 0
for h in student_heights:
    total_height += h

#len() using a for loop
num_of_students = 0
for s in student_heights:
    num_of_students += 1
    
average = total_height / num_of_students
print(round(average))
    