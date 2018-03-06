height = float(input('what is your height? (cm) '))
weight = float(input('what is your weight? (kg)'))

#convert unit from cm to m
height_cm = height / 100

#BMI calculate
BMI = weight / (height_cm * height_cm)

print('your height is: %.f (cm) = %.2f (m)' % (height, height_cm))
print('your weight is: %.f (kg)' % (weight))
print('your BMI is: %.2f' % (BMI))

#BMI check:
if BMI < 16:
    print('your are severely underweigh')
elif BMI < 18.5:
    print('you are underweigh')
elif BMI < 25:
    print('you are normal')
elif BMI < 30:
    print('you are overweight')
else:
    print('you are obese')
