my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(1, 15)
print(my_list)
my_list.extend([50, 60, 70])
print(my_list)
my_list.remove(70)
print(my_list)

sorted_my_list = sorted(my_list)
#my_list.sort()

print(sorted_my_list)

index_of_30 = my_list.index(30)

print(f"The index of the number 30 is: {index_of_30}")