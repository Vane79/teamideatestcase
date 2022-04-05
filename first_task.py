import requests
import json

api_key = '2ae929edcf167b0949e19acfc0eb7cd3'
city_id = '1503901'


def first_task():
    forecast_call = requests.get(
        f'http://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={api_key}&units=metric')
    forecast = json.loads(forecast_call.text)
    nights_temps = []
    n = 0
    while n < 40:   # На выводе всегда список длиной в сорок вложенных списков, отсюда и это число
        nested_list = []
        hour = forecast['list'][n]['dt_txt'][11:]   # Формат времени всегда одинаковый, поэтому я просто обрезаю строку без перевода в datetime
        if hour == '00:00:00' or hour == '03:00:00':
            nested_list.append(
                abs(round(forecast['list'][n]['main']['temp'] - forecast['list'][n]['main']['feels_like'], 3)))
            nested_list.append(forecast['list'][n]['dt_txt'])
            nights_temps.append(nested_list)
        n += 1
    return min(nights_temps)     # На выводе у меня список состоящий из вложенных списков дат и разностей температур


if name == 'main':
    output = first_task()
    print(
        f'Ночью {output[1][0:10]} в {output[1][11:-3]} разница между ощущаемой и реальной температурой {output[0]} градуса(ов) Цельсия.')