'''
Who likes it?
'''

#Решение
def likes(names):
    if len(names) >= 4:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    else:
        return "no one likes this"