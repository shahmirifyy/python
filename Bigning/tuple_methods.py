var= ( 1,1, 2, 45, "shahmir", False, "ali", "junaid")

# print(var)

no = var.count('shahmir')
# print(no)


index= var.index("junaid")
# print(index)


list = [1, 2, 3, 4, 5, 9, 6, 4, 10]
list.sort(reverse=True) 
print(list)

#tuples are unmuteable so it always make new tuple and return value it that tuple old tuple will not change
my_tuple = (1, 2, 3, 4, 5, 9, 6, 4, 10)
new= tuple(sorted(my_tuple, reverse=True))



print("old tuple",my_tuple)
print("new",new)