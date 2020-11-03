# what is a dictionary 
# dictionary (arrays) is another way of managing data but more dynamically 
# kay value pairs to store and manage data 
# syntax: {'name(key)': 'james(value)'}
#what type of data can be stored / manage
# any 

# let's create a dictionary 
devops_students = {
    'key' : 'value', 
    'name': 'james',
    'stream': 'tech',
    'completed_lessons' : 4,
    'completed_lesson_names': ['variables', 'operators', 'data types']
}

#display the data using key name
print(devops_students['name'])

print(devops_students.keys())
print(devops_students['completed_lesson_names'])

for _ in devops_students.keys():
    print(type(_))
