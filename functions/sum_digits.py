def sum_digits(n):
    sum_n=0
    n=str(n)
    for i in n:
        sum_n=sum_n+int(i)
    return sum_n
