# https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple

import requests
import html

from category_names import get_categories
# import json


# with open('proxy_login.json', 'r') as f_proxy_login:
#     proxy_login = f_proxy_login.read()

# proxies = {
#     'http': str(proxy_login),
#     'https': str(proxy_login)
#     }


def get_data(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('На сервере что-то пошло не так')

token_response = get_data('https://opentdb.com/api_token.php?command=request')
token = token_response['token'] 


if __name__ == '__main__':
    # data = get_data('https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple')
    categories = get_categories()
    user_category_name = input('You can choose any topic you wish: ')
    user_category_id = categories[user_category_name]

    user_number_question = input('How many questions do you want? A Maximum of 50 Questions can be retrieved per call\nPlease print a number: ')
    user_difficulty = input('What mode do you like to try: Hard, Medium, Easy or Any difficulty? ')
    data = get_data('https://opentdb.com/api.php?amount=%s&category=%s&difficulty=%s&type=multiple' % (user_number_question, user_category_id, user_difficulty))
    # import pdb; pdb.set_trace()
    # print(data)


for results_index in range(len(data['results'])):

    raw_question = 'Question: %s\n' % data['results'][results_index]['question']
    question = html.unescape(raw_question)

    raw_answers = data['results'][results_index]['incorrect_answers']
    correct_answer = data['results'][results_index]['correct_answer']
    raw_answers.append(correct_answer)
    answers = []
    for raw_answer in raw_answers:
        answer = html.unescape(raw_answer)
        answers.append(answer)

    print(question)
    for answer in answers:
        print(str(answer))
    user_input = input('Write the correct answer: ')
    if user_input == correct_answer:
        print('Congrats! Go on!')
    else:
        print('Oh Jesus... I thought you were smarter.....')
        print('The right answer is: %s\nTry next' % str(correct_answer))
    print('_______\n')    
