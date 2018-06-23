# https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple

import requests

def get_data(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('На сервере что-то пошло не так') 



if __name__ == '__main__':
    data = get_data('https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple')



for results_index in range(len(data['results'])):
    question = 'Question: %s\n' % data['results'][results_index]['question']
    answers = data['results'][results_index]['incorrect_answers']
    answers.append(data['results'][results_index]['correct_answer'])
    print(question)
    for answer in answers:
        print(str(answer))
    user_input = input('Write the correct answer: ')
    if user_input == data['results'][results_index]['correct_answer']:
        print('Congrats! Go on!')
    else:
        print('Oh Jesus... I thought you were smarter... Try this:')
    print('_______\n')    
