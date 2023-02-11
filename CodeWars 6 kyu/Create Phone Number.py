'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
'''

#Решение
def create_phone_number(n):
    #your code here
    new = []
    for i in n:
        new.append(str(i))
        f = "".join(new[0:3])
        s = "".join(new[3:6])
        t = "".join(new[6:10])
    return f"({f}) {s}-{t}"