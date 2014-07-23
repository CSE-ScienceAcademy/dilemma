'''
functions
'''

def inputData(name):
    '''
    @parameter : input a name, outputs the name
    name will be a string
    '''
    return name + '.'

def heading():
    print 'table \n'
    
def lowerCase(fname, lname):
    lower = fname.lower() + " " + lname.lower()
    return lower

def even(num):
    if num % 2 == 0:
        return 1
    else:
        return '8'
    
def vowels(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return 'true'
    else:
        return 'false'

heading()
#name = raw_input('enter a name: ')
#print inputData(name)
#print lowerCase(name, name)

name = 'david'
print name[0] 
print name[0:2] 
print name[:2] 
print name[:-2]