'''
tuples is an array (  ) that CANNOT change
list is an array [ ] that CAN change
'''
import random
days = ('Mon','Tue','Wed','Thr','Fri') #tuple
schools = ['Sci Tech','Med High','BETA','Med Tech'] #list
emptyTuple = ()
emptyList = []

print days[0] #returns a string
print schools[1] #returns a string
print days[3:] #returns a tuple of string
print schools[-1:] #returns a list of string
schools = schools + ['STPA']
print schools
a = [(1,2),(3,4),(5,6,7)]

print random.choice(schools)
print random.choice(days)
print random.randint(4,6)
print random.uniform(3,4)

