a='daBcd'
b='ABC'
a_list = list(a)
b_list = list(b)
a_new = []
flag = True
flag1 = False
for i in a_list:
    if i in b_list or i.upper() in b_list:
        flag1 = True
        a_new.append(i.upper())

    if  flag1 and i.isupper() not in b_list:
        flag = False
        print 'NO'
        break

if flag and ''.join(a_new) == b:
    print 'YES'
elif flag and ''.join(a_new) != b:
    print 'NO'