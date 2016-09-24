def partition(array, first, last):
    a = array[first]

    lb = first
    ub = last
    down = lb
    up = ub

    while up > down:
        while (not (array[down] > a)) and down < len(array) - 1:
            down += 1
        while not (array[up] <= a):
            up -= 1
        if up > down:
            temp = array[down]
            array[down] = array[up]
            array[up] = temp

    temp = array[up]
    array[up] = array[lb]
    array[lb] = temp

    j = up

    print j


a = [25, 57, 48, 37, 12, 92, 86, 33]
partition(a, 0, len(a) - 1)
print a
