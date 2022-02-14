import csv
import numpy as np
import matplotlib.pyplot as plt

n_selec = 15

def powing2(num1):
    return np.power(num1,2)


def insert_group(data_group, iter):
    if data_group.setdefault('group '+ str(iter)) == None:
        data_group['group '+ str(iter)] = []


def data_pars(data_group, command):
    result_data = []

    for item in data_group:
        if command == 'key':
            result_data.append(item)
        elif command == 'value':
            result_data.append(data_group[item])

    return result_data


def ssw(data):
    ssw_result = 0.0
    data_group = {}
    ssw_group = []

    count = 0
    iter = 0
    for item in data:
        if count == n_selec:
            ssw_result /= n_selec
            ssw_group.append(ssw_result)

            ssw_result = 0
            count = 0
            iter += 1

        insert_group(data_group, iter)
        try:
            data_group['group '+ str(iter)].append(float(item['result']))
            ssw_result += float(item['result'])
        except ValueError:
            continue

        count += 1

    ssw = 0.0
    k = 1
    for x_mid in ssw_group:
        for i in data_group['group ' + str(k)]:

            ssw += np.power(i - x_mid, 2)

        k += 1

    return data_group


def ssb(data, command):
    data_group = {}
    gl_avg = 0
    count = 0

    for item in data:
        if item['result'] != 'expr':
            count += 1

            if data_group.setdefault(item[command]) == None:
                data_group[item[command]] = []

            data_group[item[command]].append(float(item['result']))
            gl_avg += float(item['result'])
    
    print(count)
    gl_avg /= count

    ssb_result = 0
    for item in data_group:
        ssb_result += len(data_group[item]) * powing2(np.mean(data_group[item]) - gl_avg)
    
    print(ssb_result)


def boxplot(y_data, x_data, base_color="#539caf", median_color="#297083", x_label="", y_label="", title=""):
    fig, ax = plt.subplots()
    ax.boxplot(y_data , patch_artist = True
               , medianprops = {'color': median_color}
               , boxprops = {'color': base_color, 'facecolor': base_color}

               , whiskerprops = {'color': base_color}

               , capprops = {'color': base_color})

    ax.set_xticklabels(x_data)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    plt.show()


with open('atherosclerosis.csv' , 'r', encoding='utf-8') as file:
    fieldnames = ['result', 'age', 'dose']
    data = csv.DictReader(file, restkey = ',', fieldnames=fieldnames)

    res_data_group = ssw(data)
    boxplot(data_pars(res_data_group, 'value'), data_pars(res_data_group, 'key'))