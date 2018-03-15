#dictionarry
#C
person = {
#    key : value
    'name' : 'quy',
    'age' : 20,
    'ex' : 0,
    'sex' : 'male'
}

#R
'''
key = 'adfgasdf'
if key in person:
    print(person[key])
else:
    print('not found')
#print(person)
'''
'''for key in person:
    print(key, person[key])
'''

'''for value in person.values():
    print(value)
'''

for key, value in person.items():
    print(key, value)



#U

'''person['age'] = 22

print(person)'''

person['school'] = 'HUST'
