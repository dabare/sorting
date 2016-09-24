
data_list=sorted(sorted([1,2,3,433,44,55,8,5,6,7,8,9,10,11,13,14,23,4,422,4456,77,8,665,443,44,4,556,56,7,776,55,43,33,22,]))


def binary_search(list,target):
    top = len(list)-1
    bottom = 0

    while top >= bottom:
        print(list[bottom:top+1])
        mid = (top + bottom)//2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            bottom = mid + 1

        else:
            top = mid - 1

    return False

print(binary_search(data_list,556))

