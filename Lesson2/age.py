age=int(input('введите ваш возраст: '))

if age <= 6:
    print('еще маленький, в садик ходит')
if 6 <= age <= 17:
        print('Учится в школе')
if 18 <= age <= 24:
        print('Учится в университете')
if 25 <= age < 100:
    print('Работает в офисе, ну или не в офисе')  
elif age >= 100:
    print('он еще жив вообще?')   