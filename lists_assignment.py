#creating an empty list
my_list=[]
list=[50,60,70]

#adding values to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#inserting values to an existing list
my_list.insert(1, 15)
print(my_list)

#extending an existing list
my_list.extend(list)
print(my_list)

#removing a value from a list
my_list.remove(70)
print(my_list)

#sorting a list
my_list.sort()
print(my_list)

index_of_30 = my_list.index(30)
print(my_list)
print(index_of_30)