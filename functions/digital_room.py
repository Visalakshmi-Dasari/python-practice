def digital_root(n):
    def sum_num(x):
        y = str(x)
        sum_n = 0
        for i in y:
            sum_n=sum_n+int(i)
        return sum_n

    n=str(sum_num(n))

    while len(n)>1:
        n=str(sum_num(n))
    return n
