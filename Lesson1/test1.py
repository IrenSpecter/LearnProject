user={
'Andrew':{'city':'Москва','temp':'25','wind':'восточный'},
'Max':{'city':'Spb','temp':'20','wind':'северный'},
'Alex':{'city':'Amsterdam','temp':'22','wind':'северо-западный'}
}

name=input('назовите ваше имя: ')
# if name=='Alex':
# 	print(user['Alex'])
# elif name=='Max':
# 	print(user['Max'])
# elif name=='Andrew':
# 	print(user['Andrew'])
# else:
# 	print('not available')
# print(name)

# user.index('Andrew')
# user.get('Max', 'not available')
# user.get('ALex','not available')
user.get('name')
print(user.get('name'))
