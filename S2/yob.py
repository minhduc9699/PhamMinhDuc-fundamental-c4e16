import datetime
now = datetime.datetime.now()
yob = int(input("what's ur yob ?"))
age = now.year - yob
print('your age', age)

if age < 10:
    print('baby')
    print('hi')

elif age < 18:
    print('teen')

elif age == 24:
    print('lay chong')

else:
    print('not baby')


print('bye')
