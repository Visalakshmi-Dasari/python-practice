enter_weight = eval(input('enter valid weight to convert from kgs to pounds : '))
while enter_weight < 0:
    enter_weight = eval(input('impossible. Enter valid weight: '))
print('your weight in pounds: ', enter_weight*2.20462)