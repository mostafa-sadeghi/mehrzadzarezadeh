# name = input("enter a name: ")
# family = input("enter a family: ")
# total = 0
# for i in range(3):
#     new_score = float(input(f"enter score {i+1}: "))
#     total += new_score

# ave = total / 3

# print(f"{name} {family}'s average is {ave}")

# name = input("enter a name: ")
# for i in range(len(name)-1, -1, -1):
#     print(name[i], end="")


students_names = []
for i in range(5):
    new_name = input("enter a name: ")
    students_names.append(new_name)

print("first name of the list:", students_names[0])
print("last name from the list:",students_names[-1])

print(students_names)
new_name = input("enter a name: ")
students_names.append(new_name)

print(students_names)

new_name_to_delete = input("enter a name to delete: ")
for name in students_names:
    if name == new_name_to_delete:
        students_names.remove(new_name_to_delete)
print(students_names)