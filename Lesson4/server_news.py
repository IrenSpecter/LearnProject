import requests

from newsapi import NewsApiClient

# from newsapi.newsapi_auth import NewsApiAuth
# from newsapi import const
# from newsapi.newsapi_exception import NewsAPIException

# class NewsApiClient(object):

#     def __init__(self, api_key):
#         self.auth = NewsApiAuth(api_key=api_key )

#     def get_top_headlines(self, q=None, sources=None, language=None, country=None, category=None, page_size=None,
#                           page=None):
#         get_top_headlines()



newsapi = NewsApiClient(api_key='e7c29b0016ba43a09e7fcbd480457c9c')


user_input = ('Введи категорию новостей, которую ты хочешь почитать: ')
try:




# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(category='business',
                                          language='ru',
                                          country='ru')






for articles_index in range(len(top_headlines['articles'])):
    topic = 'Topic: %s\n' % top_headlines['articles'][articles_index]['source']['name']
    title = 'Title: %s\n' % top_headlines['articles'][articles_index]['title']
    description = 'Description: %s\n' % top_headlines['articles'][articles_index]['description']
    url = 'Click here for more information: %s\n' % top_headlines['articles'][articles_index]['url']
    print(topic)
    print(title)
    print(description)
    print(url)
    print('_______\n')

