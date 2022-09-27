# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30x = [ [5,2,3], [10,8,9] ] 
x = [ [5,2,3], [10,8,9] ]

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
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

def iterateDictionary2(key_name,students):
    for i in students:
        print(i[key_name])
iterateDictionary2('first_name',students)

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) 
# that, given a list of dictionaries and a key name, the function
#  prints the value stored in that key for each dictionary. For example,
#   iterateDictionary2('first_name', students) should output:


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa',
    'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 
    'Patrick', 'Minh', 'Devon']
}

def iterateCd(key_name,dojo):
    for i in (dojo[key_name]):
        print(i)
iterateCd('locations',dojo)


def iterateCd(key_name,dojo):
    for i in (dojo[key_name]):
        print(i)
iterateCd('instructors',dojo)