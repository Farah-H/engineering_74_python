# # collection in python
# # lists? 
# # we can add, remove , change an item in a list, they are MUTABLE
# # indexing starts with 0 
# #syntax: my_list = [item1, item2, ...]

# shopping_list = ['apple', 'milk', 'bread']
# print(shopping_list)
# print(type(shopping_list))

# # Managing lists
# # look at indexing in the list items 
# print(shopping_list[1])
# #print(shopping_list[start:end:step])

# # how can we add an item to our list
# shopping_list.append('eggs')
# print(shopping_list)

# # how can we remove an item from our list
# shopping_list.remove('apple')
# print(shopping_list)

# # how can we remove the item we just added later 
# shopping_list.pop()
# print(shopping_list)

# # how can i replace an ittem in my list 
# shopping_list[1] = 'fruits'

# mixed_shopping_list = [1, 2, 3, 'apple', 'milk', 'bread']
# print(mixed_shopping_list)

#task 
# create mixed data list of 7 items 
# display type of data
# add delete replace pop


# my_mixed_list = [1, 2.4, [1,3,4] , 'potato', 'porridge', 6.7, 10]

# for _ in my_mixed_list:
#     print(_, type(_))

# #add
# my_mixed_list.append(600)
# print(my_mixed_list)

# #delete
# my_mixed_list.remove('potato')
# print(my_mixed_list)

# #replace
# my_mixed_list[1] = 'tomatoes'
# print(my_mixed_list)

# #pop
# my_mixed_list.pop()
# print(my_mixed_list)

# # use indexing to print the list in reverse order 
# print(my_mixed_list[::-1])

# Tuples are IMMUTABLE - can't be changed 
# Use case NI number, DOB, place of birth
# Sytax: we use commas to declare a tuple, but standard practice is also to encapsulate a tuple in ()

short_list = ('paracetemol', 'eggs', 'supermalt')
print(type(short_list))

#short_list[1] = 'fruits' 

print(short_list[-1])