def fibonacci():
    x = 0
    y = 1
    print x
    print y
    for i in range(10):
        z = x + y**2
        print z
        x = y
        y = z

fibonacci()
print('Test')
