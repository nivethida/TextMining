t# -*- coding: utf-8 -*-
course = ['math','history','physics','chemistry']
print(course[0])
print(course[-1])

print(course[1:3])

print(course[:3])

print(course[-3:])

print('math' in course)
print('geography' not in course)


#appending

course.append('musics')

print(course)

#appending in the front "inser"

course.insert(0, "geography")

print(course)

course.insert(2, "geography")

print(course)

# reversing a list
print(course[::-1])

#even and odd indices

print(course[0::2])

#tuples

course = ('math','history','physics','chemistry')

a,b,c,d = course

a,b,c = b,c,a


#set 


course = {'math','history','physics','chemistry', 'math'}

print(course)


# print(list(set(course))) to remove duplicates from list

course1 = ['math','history','physics','chemistry']
course2 = ['math','music']

# intersection
print(list(set(course1) & set(course2)))

#union
print(list(set(course1)| set(course2)))

#difference
print(set(course1) - set(course2))

#Dictionaries are used to store key value pairs, usually used to descibe features of some objects

dct1 = {'1st value' : 1,
        '2nd value': 2,
        '3rd value': 'three'}

for i in dct1.keys():
    print(i)
    

for i in dct1.values():
    print(i) 
    
#tuples from dict    
for i in dct1.items():
    print(i) 
    
    
dict2 = {}

dict2["length"] = 10   

dict2["breadth"] = 20

dict2['height'] = 40

print(dict2)

# if statement

language = 'python'

if language == 'python':
    print('yes')
    
elif language == 'scalar':
    print('not used')
    
else:
    print('none')
    
#inline if

x = 8
y = 2

z = x/y if y!=0 else "division by zero"

print(z)    
        
#try and except
x = 8
y = 0

try:
    z = x/y
    print(z)
    
except:
    print('something is wrong') 
    

x = 'one'
y = 2

try:
    z = x/y
    print(z)
    
except ZeroDivisionError:
    print('ZeroDivisionError')  
    
except TypeError:
    print('value mismatch')

except:
    print('something else is wrong')

# iterations
    
for i in [1,2,3]:
    print(i)

for i in range(10): # 0 to 9
    print(i)
    
for index, value in enumerate('BAN675'):
    print("the {}th value is {}".format(index, value))
    
# enumerate
x = [1,2,3,4,5,6,7,8,9]
y = [i for i in x if i%2==1]
print(y)    




























