student_name = ["Sai","Rahul","Rohit","Sita","Gita","Ravi","Kumar"]

# Print Rohit from the list
print(student_name[2])




# Print tihoR from the list
for name in student_name:
    if name in student_name[2]:
        print(name[::-1])


for name in student_name:
    if name == "Rohit":
        print(name[::-1])

print(student_name[2][::-1])



# Print h from rohit

for name in student_name:
    if name in student_name[2]:
        print(name[2])


for name in student_name:
        if name == student_name[2]:
             print(name[2])

print(student_name[2][2])
