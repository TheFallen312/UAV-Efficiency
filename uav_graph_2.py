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
    results.append([])
    for l in length:
        
        results[UAV_n].append(a[UAV_n][0])
        smax =  ((v/0.28)*tm)*(h/1000)
        print(smax)
        sq = ((l/1000)**2)
        print(sq)
        n_min = sq/smax
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
        if n_max - int(n_max) >= 0.5:
            maxr = int(n_max)+1
        else:
            maxr = int(n_max)
        for n in range(int(n_min),maxr,step_n):
            n_vec.append(n)
        #n_vec.pop(0)
        if n_vec[0]<1:
            n_vec[0] = 1
        if n_vec[1] == 1:
            n_vec.pop(1)

        n_vec.append(n_max)
        print(n_vec)
        results[UAV_n].append(round(n_min,4))
        results[UAV_n].append(n_max)
        results[UAV_n].append(step_n)
        for n in n_vec:
            t = 0

            x = l/n
            noc = int(x)//h #количество "столбцов" в сетке
            nos = l//h #количество "строк" в сетке
            print(h)
            #print(x)
            #print(noc)
            print(l)
            print(n)
            print(nos)
            '''
            if x%h > x//2:
                noc = noc + 1
            if l%h > x//2:
               nos = nos + 1
            '''
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
        print(results)

 
with open('UAV_output.csv','w',newline='') as f:
	results_writer = csv.writer(f,delimiter=';',quotechar="'",quoting = csv.QUOTE_NONNUMERIC)
	for UAV_n in range(len(a)):
		results_writer.writerow(results[UAV_n])
