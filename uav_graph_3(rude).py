from anneal import SimAnneal
import numpy
import matplotlib.pyplot as plt
import random
import csv
import math



a = []
with open('UAV_input.csv', newline='') as f:
    reader = csv.reader(f, dialect = 'excel', delimiter = ';')
    
    for row in reader:
    	a.append(row)



#l = 1000 #линейный размер зоны(м)
results = []
length = [500,1000,5000,10000,15000]
for UAV_n in range(len(a)):
    
    v = 0.28*float(a[UAV_n][1])  #линейная скорость БПЛА(км/ч)
    h = int(a[UAV_n][3]) #линейный размер зоны просмотра БПЛА(м)
    tm = float(a[UAV_n][2])
     #количество БПЛА в группе
    
    for l in length:
        results.append([])
        results[UAV_n].append(a[UAV_n][0]) 
        n_min = ((l/1000)**2)/((v/0.28)*tm)/(h*1000)
        n_max = l/(h*2)
        print(round(n_min,6))
        print(n_max)
        n_vec = []
        step_n = 0
        for n in range(int(n_min),int(n_max)):
            if n > 10:
                step_n = int(n_max)//5
            else:
                step_n = 1
        print(step_n)
        for n in range(int(n_min),int(n_max),step_n):
            n_vec.append(n)
        n_vec.pop(1)
        n_vec.pop(0)
        
        n_vec.insert(0,1)
        n_vec.append(n_max)
        print(n_vec)
        results[UAV_n].append(round(n_min,4))
        results[UAV_n].append(step_n)
        for n in n_vec:
            t = 0

            x = l/n
            sq = 
            t = (sa.best_fitness/v)/3600

            results[UAV_n].append(round(t,4))
        print(results)

 
with open('UAV_output.csv','w',newline='') as f:
	results_writer = csv.writer(f,delimiter=';',quotechar="'",quoting = csv.QUOTE_NONNUMERIC)
	for UAV_n in range(len(a)):
		results_writer.writerow(results[UAV_n])
