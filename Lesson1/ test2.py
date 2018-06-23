user={
'Alexey':{'city':'Moscow', 'temp':'25','wind':'west'},
'Mary':{'cuty':'Berlin', 'temp':'22','wind':'east'},
'Lary':{'city':'Texas','temp':'29','wind':'south'}
}

name=input('введите ваше имя: ')
print(user.get(name))
