from anneal import SimAnneal
import numpy
import matplotlib.pyplot as plt
import random
import csv

a = []
with open('UAV_input.csv', newline='') as f:
    reader = csv.reader(f, dialect = 'excel', delimiter = ';')
    
    for row in reader:
    	a.append(row)

print(a)
print(float(a[0][1]))