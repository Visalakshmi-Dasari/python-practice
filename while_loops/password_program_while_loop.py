password = 'vishdee'
i=0
while i < 5:
    enter_password = input('enter password: ')
    if enter_password == password:
        print('you are logging in....')
        break
    else:
        print('valid password')
    i = i + 1
print('kicked off')
