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


# #display the data using key name
# print(devops_students['name'])

# print(devops_students.keys())
# print(devops_students['completed_lesson_names'])

# for _ in devops_students.keys():
#     print(type(_))

# devops_students['completed_lessons'] = 3
# print(devops_students['completed_lessons'])
# print(type(devops_students.items()))


# task 
 


# display data in reverse order of hobby list 

# create a new dictionary to store user details
# all the details that you utilised in thhe alst task curse, grades
user_details = {
    'name': 'Farah Moshref Hassan',
    'DOB': '31/08/1998',
    'age': 22,
    'address' : '9 Something Lane, London, NS3 568',
    'national_insurance' : 'DH6735H',
    'highest_qualification' : 'MSc Nuclear Science and Engineering',
    'hobbies' : ['Painting', 'Gaming', 'Volunteering'], #create a list of hobbies of at least 3 items
    'course' : 'DevOps',
    'grades' : {
        'English' : 'A*',
        'Science' : 'A*',
        'Art' : 'B',
        'Chemistry' : 'A'
    }
}

# adding item to list inside dictionary 
print(user_details['hobbies'])
user_details['hobbies'].append('Sleeping')
print(user_details['hobbies'])

# removing item from list inside dictionary 
user_details['hobbies'].remove('Sleeping')
print(user_details['hobbies'])

print(user_details['hobbies'][::-1])