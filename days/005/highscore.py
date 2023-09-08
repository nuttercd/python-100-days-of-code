# This challenge needs to be completed without using the max() or min() functions
# Inputs 78 65 89 86 55 91 64 89

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#Highest Score
high_score = 0
for h in student_scores:
    if (h > high_score):
        high_score = h
        
print(high_score)