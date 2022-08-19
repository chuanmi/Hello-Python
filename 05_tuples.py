### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "chuanmi", "Moreno", "chuanmi")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("chuanmi"))
print(my_tuple.index("Moreno"))
print(my_tuple.index("chuanmi"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

tpl = ("Canyon", "Giant", "Trek")
print(len(tpl))

# ------------------------------------------------------------------------
# E1
tuple =()
print(tuple)

# E2
sisters = ("Sheila", "Natalia")
brothers = ("Fran", "Pepe")

# E3
siblings = sisters + brothers
print(siblings)

#E4
print(len(siblings))

# E5
siblings = list(siblings)
siblings.append("Enrique")
siblings.append("Pepi")
print(type(siblings))
print(siblings)

siblings = (*siblings,)
print(siblings)
print(type(siblings))