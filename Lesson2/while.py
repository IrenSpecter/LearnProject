data = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
while data:
    name = data.pop()
    if name == 'Валера':
        print('Валера нашелся!')
        break
else:
    print('Валеры в списке нет')