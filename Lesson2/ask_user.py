def ask_user():
    while True:
        text = input('Как дела? ')
        if text == 'Хорошо':
            print('Так держать!')
            break

ask_user()

def get_answer():
    while True:
        question = input(' ')
        answer = {
        'привет': 'И тебе привет!', 
        'как дела?': 'Лучше всех', 
        'что делаешь?':'с тобой болтаю!'
        }
        if question == 'Пока!':
            print('Гудбай май лав, гудбай!')
            break
        else:
            print(answer.get(question.lower()))

get_answer()