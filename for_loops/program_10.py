def rectangle():
    lenght_of_rectangle = int(input('Enter length of rectangle: '))
    breadth_of_rectangle = int(input('Enter breadth of rectangle: '))
    print('*' * lenght_of_rectangle)
    for i in range(breadth_of_rectangle):
        print('*',' '*(lenght_of_rectangle-4),'*')
    print('*' * lenght_of_rectangle)

rectangle()
