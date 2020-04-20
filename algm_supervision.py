from itertools import combinations
import csv
import math
import os

l2 = []
l = []
l3 = []



# From here the old program run methods above are for optimization
"""This method calculate the distance between two health centers of the same healthZone 
Takes as input a tuple containing lat, log data"""
def calculate_distance(tup1, tup2):
	tup = ()
	if(tup1[2] and tup1[3]	and tup2[2] and tup2[3]  != ''):
		latitude1 = float(tup1[2])
		longitude1 = float(tup1[3])
		latitude2 = float(tup2[2])
		longitude2 = float(tup2[3])
		dlat = latitude2 - latitude1
		dlong = longitude2 - longitude1
		d1 = math.sqrt((dlat**2) + (dlong**2))
		dkm = (d1 * 111.139) * 1000
		
		if dkm < 100:
			tup = (tup1, tup2, dkm)
	return list(tup)

"""Thise method just run a product of run that is n*n comparision are made and the resulting pair are fed to the calculate method"""
def algm():
	with open("mars 2020.csv", encoding="utf8", errors='ignore') as file:
		reader = csv.reader(file)
		for col in reader:
			tup2 = (col[3], col[5], col[6], col[7])
			l.append(tup2)
		#aproduct = combinations(l, l)
		for alem, blem in combinations(l,2):
			if(alem[0]==blem[0]):
				#print(str(alem[2])+ "--->" + str(blem[2]))
				l2.append(calculate_distance(alem, blem))
				


	with open('result_mars_2020 50 3.csv', 'w', newline='') as file2:
		writer = csv.writer(file2)
		for r in l2:
			if r != []:
				li = [r]
				writer.writerows(li)

if __name__ == '__main__':
    algm()	