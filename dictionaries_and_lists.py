# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30x = [ [5,2,3], [10,8,9] ] 


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x [1][0]=15
print(x)

students[0]['last_name']="Bryant"
print(students)

sports_directory['soccer'][0]="Andres"
print(sports_directory)

z[0]['y']=30
print(z)


# Create a function iterateDictionary(some_list) that, given a list of dictionaries,
#  the function loops through each dictionary in the list and prints each key and
# the associated value. 


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(students):
    for i in range(len(students)):
        print(students[i])
iterateDictionary(students)