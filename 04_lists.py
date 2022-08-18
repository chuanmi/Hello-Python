### Lists ###

my_list = list()
my_other_list =[]

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print (my_list)
print(len(my_list))

my_other_list = [41, 1.78, "chuanmi", "Moreno"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("chuanmiDev")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))
