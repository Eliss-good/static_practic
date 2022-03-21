import csv
from math import pow, sqrt
from line_regres import data_fram_regres
import graph
import numpy as np

class data_paramerts:
    def __formated_to_array(self, dict_dates, command):
        arr_new = np.array([])

        for item in dict_dates:
            arr_new = np.append(arr_new, float(item[command]))
        return arr_new


    def __quad_deviation(self):
        chislitel = 0
        for item in self.arr_data.flat:
            chislitel += pow((item - self.average),2)

        return sqrt(chislitel/(self.arr_data.size -1)) 


    def __init__(self, new_arr_data, command):
        self.arr_data = self.__formated_to_array(new_arr_data,command)
        self.average = np.average(self.arr_data)
        self.deviation = self.__quad_deviation()
        self.name = command


def open_csv(command):
    with open('states.csv' , 'r', encoding='utf-8') as file:
        fieldnames = ['state' , 'metro_res', 'white' , 'hs_grad', 'poverty', 'female_house']
        data = csv.DictReader(file, restkey = ',', fieldnames=fieldnames)
        
        dp = data_paramerts(data, command)
        return dp

data1 = open_csv('hs_grad')
data2 = open_csv('poverty')

frame_regres = data_fram_regres(data1,data2)
graph.set_graph(data1, data2, frame_regres.y_fun_data, frame_regres.arr_remains)