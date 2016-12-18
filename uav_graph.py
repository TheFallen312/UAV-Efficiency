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

for UAV_n in range(len(a)):
    results.append([])
    v = 0.28*float(a[UAV_n][1])  #линейная скорость БПЛА(км/ч)
    h = int(a[UAV_n][3]) #линейный размер зоны просмотра БПЛА(м)
    n = int(a[UAV_n][5]) #количество БПЛА в группе
    
    l = 400
    t = 0
    while t < float(a[UAV_n][2]): 
        x = l//n
        noc = x//h #количество "столбцов" в сетке
        nos = l//h #количество "строк" в сетке
        
        if x%h > x//2:
            noc = noc + 1
        if l%h > x//2:
            nos = nos + 1
        
        s = noc * nos #количество "узлов" в сетке
        
        coords = numpy.zeros((s,2))

        for i in range(int(nos)):
            for j in range(int(noc)):
    	        coords[noc*i + j][0] = float(j*h)
    	        coords[noc*i + j][1] = float(i*h)

        sa = SimAnneal(coords)
        sa.Anneal()
        t = (sa.best_fitness/v)/3600
        results[UAV_n].append(round(t,4))
        l = l * math.sqrt(2)
    print(results)

 
with open('UAV_output.csv','w',newline='') as f:
	results_writer = csv.writer(f,delimiter=';',quotechar="'",quoting = csv.QUOTE_NONNUMERIC)
	for UAV_n in range(len(a)):
		results_writer.writerow(results[UAV_n])
