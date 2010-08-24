import csv,itertools
import time

with open("/home/ilich/Scaricati/Peso.csv","r") as f:
    pesi=[t for t in csv.reader(f)][1:]
    peso7=itertools.izip(*[itertools.islice(pesi, i, None, 7) for i in range(7)])
    #pesoM=[(time.mktime(time.strptime(week[6][0],"%m/%d/%Y %H:%M:%S")),reduce(lambda x,y: x+float(y[1]),week,0.0)/7.0 )for week in peso7]
    pesoM=[(week[6][0],reduce(lambda x,y: x+float(y[1]),week,0.0)/7.0 )for week in peso7]
    with open("/home/ilich/Documenti/pesi_media.csv","w+") as g:
        csvW = csv.writer(g)
        for p in pesoM:
            csvW.writerow(p)
        




    

    
