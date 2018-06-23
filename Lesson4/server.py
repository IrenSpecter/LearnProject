from datetime import datetime

from flask import Flask, abort, request # abort - прекратить

from news_list import all_news

from get_weather import get_weather_213


city_id = 524901
apikey = '713df0290b743a025e28c1f74b3a12af'


app = Flask(__name__)

@app.route('/') #главная страница /
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric' % (city_id, apikey)
    weather = get_weather_213(url)
    cur_date = datetime.now().strftime('%d.%m.%Y')
    print(cur_date)

    result = '<p><b>Температура:</b> %s\n</p>' % weather['main']['temp']    # <p> </p> - параграф, <b> </b> - выделение
    result += '<p><b>Город:</b> %s</p>' % weather['name']
    result += '<p><b>Дата:</b> %s</p>' % cur_date
    return result


@app.route('/news')
def all_the_news():
    colors = ['green', 'red', 'blue', 'magenta']
    try:
        limit = int(request.args.get('limit', 0)) # мы положили в перелменную limit то, что содержится в args по ключу limit, либо слово all
    except:
        limit = 10
    color = request.args.get('color') if request.args.get('color') in colors else 'black'
    # for item in request.args:
    #     print(item)
    #     print(request.args.get(item))
    return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color,limit)


@app.route('/news/<int:news_id>') #шаблон, после news/ должно еще что-то идти
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id] #пройдись по списку и выбирай элемент, если услование выполняется, 
    #то запиши результат конструкции в переменную news
    if len(news_to_show) == 1:
        result = '<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>' # h1 - главыный заголовок страницы, в него вписываем именованный символ подстановки
        result = result % news_to_show[0]
        return result
        # return 'Новость: %s' % news_id #у фласка всегда должна быть строка
    else:
        abort(404)   


if __name__ == '__main__':
    app.run(port=5000, debug=True)