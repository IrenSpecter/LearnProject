import requests


def get_weather_213(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Что-то пошло не так')    


if __name__ == '__main__':
    data = get_weather_213('https://api.openweathermap.org/data/2.5/weather?id=524901&APPID=713df0290b743a025e28c1f74b3a12af&units=metric')
    print(data)