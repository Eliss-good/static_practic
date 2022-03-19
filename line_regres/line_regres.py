from math import sqrt
import numpy as np

class data_fram_regres:
    def __init__(self, first_data, second_data) -> None:
        self.x_data = first_data
        self.y_data = second_data
        
        self.correl()
        self.find_b1_coef_line()
        self.find_b0_coef_line()
        self.find_line()

        self.standart_mistake()
        self.fun_mistake_b1()
        self.fun_mistake_b0()
        self.fun_t_b1()
        self.fun_t_b0()
        self.calcul_remains()


    def correl(self):
        size_arr = self.x_data.arr_data.size
        chislitel = 0

        for i in range (0, size_arr):
            chislitel += (self.x_data.arr_data[i] - self.x_data.average) * (self.y_data.arr_data[i] - self.y_data.average)

        self.crorrel = chislitel/((size_arr - 1) * self.x_data.deviation * self.y_data.deviation) 


    def find_b1_coef_line(self):
        self.b1 = (self.y_data.deviation/self.x_data.deviation) * self.crorrel


    def find_b0_coef_line(self):
        self.b0 = self.y_data.average - self.x_data.average * self.b1


    def find_line(self):
        x = self.x_data.arr_data

        y_fun = self.b1 * x + self.b0
        self.y_fun_data = y_fun


    def standart_mistake(self):
        chislitel = 0

        for i in range(0, self.y_data.arr_data.size):
            chislitel += pow(self.y_data.arr_data[i] - self.y_fun_data[i], 2)

        self.mistake_model = sqrt(chislitel / (self.y_data.arr_data.size -2))

    def fun_mistake_b1(self):
        znam = 0

        for item in self.x_data.arr_data.flat:
                znam += pow((item - self.x_data.average),2)
        
        self.mistake_b1 =  self.mistake_model / sqrt(znam)


    def fun_mistake_b0(self):
        znam = 0
        chislitel = 0

        for item in self.x_data.arr_data.flat:
                chislitel += pow(item, 2)
                znam += pow((item - self.x_data.average),2)
        
        self.mistake_b0 = self.mistake_model * (sqrt(chislitel) / sqrt(self.x_data.arr_data.size * znam))

    
    def fun_t_b1(self):
        self.t_b1 = self.b1 / self.mistake_b1

    
    def fun_t_b0(self):
        self.t_b0 = (abs(self.b0)/ self.mistake_b0)


    def calcul_remains(self):
        self.arr_remains = np.array([])
        
        for i in range (0, self.y_fun_data.size):
            self.arr_remains = np.append(self.arr_remains, self.y_data.arr_data[i] - self.y_fun_data[i])
        print(self.arr_remains)
        

