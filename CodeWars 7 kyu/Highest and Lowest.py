'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

#Решение
def high_and_low(numbers):
    new_lst = []
    new_max_and_min_str = []
    numbers = numbers.split()
    for i in numbers:
        new_lst.append(int(i))
    new_max_and_min_str.append(str(max(new_lst)))
    new_max_and_min_str.append(str(min(new_lst)))
    return ' '.join(new_max_and_min_str)