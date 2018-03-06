import datetime
now = datetime.datetime.now()
yob = int(input("what's ur yob ?"))
age = now.year - yob
print('your age', age)
