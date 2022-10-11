arr = [-5, -1, 0, 3, 8, 22, 54]
s1 = 2 # can find
s2 = 6 # can`t find

def sum_in_arr(arr,S):
    j = len(arr) - 1
    i = 0
    k = 0
    while i < j:
        if arr[i] + arr[j] == S:
            k = 1
            break
        elif arr[i] + arr[j] < S:
            i += 1
        else:
            j -= 1
    if k == 0:
        print('-1')
    else:
        print(arr[i],' + ', arr[j], ' = ', S)


def sum_in_arr_1(arr, S):
    k = 0
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j] == S):
                k = 1
                print(arr[i],' + ', arr[j], ' = ', S)
    if k == 0:
        print('-1')


sum_in_arr(arr, s1)
sum_in_arr(arr, s2)
sum_in_arr_1(arr, s1)
sum_in_arr_1(arr, s2)