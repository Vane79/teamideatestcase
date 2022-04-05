import requests
import json
import datetime

api_key = '2ae929edcf167b0949e19acfc0eb7cd3'
latitude = '55.3333'
longitude = '86.0833'


def second_task():
    times_call = requests.get(
        f'http://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=current,minutely,hourly,alerts&appid={api_key}')
    whole_json = json.loads(times_call.text)
    output_list = []
    n = 0
    while n < 5:
        nested_list = []
        sunrise = datetime.datetime.fromtimestamp(whole_json['daily'][n]['sunrise'])
        sunset = datetime.datetime.fromtimestamp(whole_json['daily'][n]['sunset'])
        nested_list.append(str(sunset - sunrise))
        nested_list.append(str(sunrise.date()))
        output_list.append(nested_list)
        n += 1
    return max(output_list)


if name == 'main':
    timediff = second_task()
    print(f'{timediff[1]} наиболее длинный день из ближайших пяти дней в Кемерове. Длина этого дня составит {timediff[0]} ')