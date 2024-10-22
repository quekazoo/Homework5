def good_name(ban_name):
    keywords = ['and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
    'else', 'except', 'exec', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
    'is', 'lambda', 'nonlocal', 'not', 'None', 'or', 'pass', 'print', 'raise', 'return', 'True',
    'try', 'while', 'with', 'yield']

    if ban_name in keywords:
        return False

    if ban_name[0].isdigit():
        return False

    if ban_name.count('_') > 1:
        return False

    for char in ban_name:
        if not (char.islower() or char.isdigit() or char == '_'):
            return False

    return True

# ban_name = input("Введите имя переменной: ")
# print(good_name(ban_name))