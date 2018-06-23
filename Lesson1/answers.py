def get_answer(question,answer):
    return answer.get(question.lower())



question=input(' ')
answer={'привет': 'И тебе привет!', 'как дела?': 'Лучше всех', 'пока': 'Увидимся'}
print(get_answer(question,answer))
