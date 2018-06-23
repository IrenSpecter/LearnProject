import requests


def get_news_213(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('What`s wrong with you?')   


if __name__ == '__main__':
    data = get_news_213('https://newsapi.org/v2/top-headlines?country=&category=business&apiKey=e7c29b0016ba43a09e7fcbd480457c9c')
    print(data)