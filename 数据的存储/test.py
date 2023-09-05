from random import randint


with open('D:\CPP\职工管理系统\职工管理系统\Empfile.txt', 'w', encoding='utf-8',) as file:
    for id, name in zip(range(1, 100+1), range(1, 100+1)):
        message = f"{id} {name} {randint(1,3)}\n"
        file.write(message)
