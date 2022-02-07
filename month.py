import json
import numpy as np
import matplotlib.pyplot as plt

class City_W(object):
    def __init__(self, id):
        self.id = id
        self.day_list = []
        self.temp_day = []


    def init_temp(self, n_temp, day_last):
        self.temp_day.append(n_temp)
        self.day_list.append(day_last)


    def avg_temp_fun(self):
        if len(self.temp_day) != 0: 
            self.avg = np.meam(self.temp_day)
    

    def math_hold_fun(self):
        self.mathavg = 0
        for i in range(0, len(self.temp_day)):
            self.mathavg += (self.temp_day[i] - self.avg) / len(self.temp_day) 


def lable_control(n_id):
    with open('lablel_data.json','r') as file:
        data = json.load(file)

    return data[n_id]


def addgraph(static_city):
    for i in static_city:
        plt.plot(i.day_list, i.temp_day, label = lable_control(i.id) )

    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


def transftype(str):
    if str[0] == '+':
        str = str.replace('+', '')
        return int(str)

    elif str[0] == '-':
        str = str.replace('-', '')
        return int(str)*(-1)


def cheack(avgr1, **kwargs1):
    count = 0

    for i in avgr1:
        if i.id == kwargs1['tid']:
            i.init_temp(transftype(kwargs1['temp']), kwargs1['date'])
            count += 1
            break
    
    if (count == 0):
        n_type =  City_W(kwargs1['tid'])
        n_type.init_temp(transftype(kwargs1['temp']), kwargs1['date'])

        avgr1.append(n_type)


def start_prog(data):
    static_city = []

    for i in range(0, len(data)):
        if data[i]['tod'] == '2':
            cheack(static_city, **data[i])

    addgraph(static_city)

    for i in static_city:
        addgraph(i.temp_day)


with open('weather_date.json','r') as file:
    data = json.load(file)

start_prog(data)