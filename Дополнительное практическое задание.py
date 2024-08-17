grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students_GPA={}
list_students=list(students)
list_students.sort()
print(list_students)
students_GPA.update({list_students[0]:sum(grades[0])/len(grades[0]), list_students[1]:sum(grades[1])/len(grades[1]),list_students[2]:sum(grades[2])/len(grades[2]),list_students[3]:sum(grades[3])/len(grades[3]),list_students[4]:sum(grades[4])/len(grades[4])})
print(students_GPA)







