import requests


def get_data(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('На сервере что-то пошло не так')


def get_categories():
    categories_trivia = get_data('https://opentdb.com/api_category.php')
    raw_categories = categories_trivia['trivia_categories']

    categories = {}

    for raw_category in raw_categories:
        category_id = raw_category['id']
        category_name = raw_category['name']
        categories[category_name] = category_id
    return categories 
