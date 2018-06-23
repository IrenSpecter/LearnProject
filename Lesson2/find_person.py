data = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name):
    while data:
        name2 = data.pop()
        if name == name2:
            return 'Ваше имя в списке'
    else:
        return 'Вас в списке нет'

name1=input('Введите имя: ')
print(find_person(name1))