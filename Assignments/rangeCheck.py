def ran_check(num,low,high):
    return low<=num<=high

def ran_check_flag(num,low,high):
    if low<=num<=high:
        print('Number is within range')
    else:
        print('Number is not within range')
    '''
    #Another way of doing the same thing
    if num in range(low,high):
        print('Number is within range')
    else:
        print('Number is not within range')'''

print(ran_check(1,1,5))
ran_check_flag(2,1,5)