import random
from random import choice
from random import randint
rand_list = []
for i in range(11):
    rand_list.append(random.randint(1, 6))

# rand_list = [4,5,5,6,4,3,2,4,5,5,6,6,5,3,3,4]

def lucky_check(rand_list):
    print(rand_list)
    lucky = []
    j = 0
    for i in rand_list:
        if i > 4 and j < 5: # if our element i = 5 or 6, and the previous element j < 5 this means we need to start a new series
            lucky = []
            lucky.append(i)
        elif i > 4: # elif our element = 5 or 6, and the previous element j = 5 or 6 this means we continue our series
            lucky.append(i)
        j = i
    print(lucky) # to check our series
    if lucky.count(lucky[0]) == len(lucky):
        print("0")
    else:
        print(lucky)



series = ''.join(choice('123456') for i in range(10))
# series = '4556432455665334'


def lucky_check_1(series):
    print(series)
    lucky = ''
    j = '0'
    for i in series:
        if (i == '5' or i == '6') and j != '5' and j != '6': # if our element i = 5 or 6, and the previous element j < 5 this means we need to start a new series
            lucky = ''
            lucky = lucky + i
            # print('i',i,'j',j,'lucky',lucky)
        elif i == '5' or i == '6': # elif our element = 5 or 6, and the previous element j = 5 or 6 this means we continue our series
            lucky = lucky + i
        j = i
    print(lucky) # to check our series

    if len(lucky) < 1 or len(lucky) == lucky.count(lucky[0]):
        print("0")
    else:
        print(lucky)
lucky_check(rand_list)
lucky_check_1(series)