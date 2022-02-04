import json
import numpy

class City_W(object):

    def __init__(self, id, day_start):
        self.id = id
        self.day_start = day_start
        self.temp_day = []
        self.day_last = ''

    def init_temp(n_temp, day_last):
        self.temp_day.append(n_temp)
        self.day_last = day_last


def transftype(str):
    if str[0] == '+':
        str = str.replace('+', '')
        return int(str)

    elif str[0] == '-':
        str = str.replace('-', '')
        return int(str)*(-1)


def cheack(*avgr1, **kwargs1):
    count = 0

    for i in range(0,len(avgr1)):
        n_city = avgr1[i]
        if n_city.id == kwargs1['tid']:
            avgr1[i].init_temp(transftype(kwargs1['temp']), kwargs1['date'])
            count += 1
            break
    
    if (count == 0):
        n_type =  City_W(kwargs1['tid'], kwargs1['date'])
        n_type.init_temp(transftype(kwargs1['temp']), kwargs1['date'])

        avgr1.append(n_type)

def start_prog(data):
    static_city = []
    for i in range(0, len(data)):
        cheack(static_city, **data[i])
    
city_id = {'53':'Samara', '54': 'Saint-Petarsburg', '35': 'Moscow'}
with open('weather_date.json','r') as file:
    data = json.load(file)
start_prog(data)