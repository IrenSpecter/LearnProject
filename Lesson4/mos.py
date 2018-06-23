import requests

from flask import Flask, abort, request



def get_data(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Что-то пошло не так')   


if __name__ == '__main__':
    data = get_data('https://apidata.mos.ru/v1/datasets/658?api_key=314f0244eafcb21f6fbaeb1d2f33b516')
    print(data)