# https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple

import requests
import html
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from quiz_bot_key import main

from category_names import get_categories

# import json

def load_data():
    # return json.load(open(filepath, 'r'))
    with open('proxy_login.json', 'r') as f_proxy_login:
        proxy_login = f_proxy_login.read()
    proxies = {
        'http': str(proxy_login),
        'https': str(proxy_login)
        }
    return proxies


def get_data(url, proxies):
    data = requests.get(url, proxies)
    if data.status_code == 200:
        data = data.json()
        if data.get('response_code') == 0:
            results = data.get('results')
            return result
        else:
            print('Something went wrong')
    else:
            print('Server is not responding now and something has broken.')


def greet_user():
    hello = 'Hello, darling! I am Crazy Quiz Bot. \nI know many fun questions from all over the world. \nLet`s do it!'
    print(hello)
    update.message.reply_text(hello)
    if user_text == update.message.text:
      print(user_text)
      update.message.reply_text(user_text)


# def talk_to_me(bot, update): # повторяет функцию выше
#     user_text = update.message.text 
#     print(user_text)
#     update.message.reply_text(user_text)


def get_user_questions(): 
    # data = get_data('https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple')
    greet_user()
    categories = get_categories()
    user_category_name = input('You can choose any topic you wish: ')
    user_category_id = categories[user_category_name]

    # user_number_question = input('How many questions do you want? A Maximum of 50 Questions can be retrieved per call\nPlease print a number: ')
    user_difficulty = input('What mode do you like to try: Hard, Medium, Easy or Any difficulty? ')
    data = get_data('https://opentdb.com/api.php?amount=2&category=%s&difficulty=%s&type=multiple' % (user_category_id, user_difficulty))
    # import pdb; pdb.set_trace()


def print_questions(results):
    data = get_data()
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

    user_choice_continue = input('Well done! Bro, do you want to continue? ')
    return user_choice_continue


if __name__ == '__main__':
    PROXY = load_data()
    user_choice_continue = 'yes'
    while user_choice_continue == 'yes':
        user_questions_api = get_user_questions()
        # result_quiz = get_data(user_questions_api, PROXY)
        answers_questions = print_questions(result_quiz)
    else:
        print('Okey and Buy. I will miss you.')


