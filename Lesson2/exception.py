# import time

# def do_something(x):
#     try:
#         print(x)
#     except KeyboardInterrupt:
#         print('привет')
#         time.sleep(1)

# x = 0
# while x < 10:
#     do_something(x)
# x += 1

answers = {
        'привет': 'И тебе привет!', 
       'как дела?': 'Лучше всех', 
        'что делаешь?':'с тобой болтаю!'
        }


def get_answer(question,answers):
    try:
        return (answers[question])
    except KeyError:
        return 'Я тебя не понимаю'


def ask_user(answers):
    while True:
        try:
            user_input = input('Скажи что-нибудь:\n')
            if user_input == 'Пока':
                print('Гудбай май лав, гудбай!')
                break
            else:       
                answer = get_answer(user_input, answers)
                print(answer)
        except KeyboardInterrupt:
            print('Как жаль, что ты уже уходишь!')
            break

ask_user(answers)