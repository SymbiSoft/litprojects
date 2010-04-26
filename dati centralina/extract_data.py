from itertools import groupby
import random, sys, csv, os
from math import floor

fileName = sys.argv[1]
message = "%s -> %s righe"

with open(fileName,"r") as f:
	csvR = csv.reader(f)

        sdata=sorted([(round(i),round(j*4/1000)*1000/4,k) for i,j,k in [map(float,tuple(t)) for t in csvR]])
        print message % (fileName, len(sdata))

        gdata=[]
        for k,g in groupby(sdata,lambda t: t[:2]):
                l=list(g)
                gdata.append(k+(round(reduce(lambda acc, t: acc+t[2], l, 0.0)/float(len(l)), 2),))

        s=list(os.path.splitext(fileName))
        s.insert(1,".min")
        sFileName ="".join(s)
        with open(sFileName,"w+") as f:
                csvW= csv.writer(f)
                for row in gdata:
                        csvW.writerow(row)                  
                print message % (sFileName, len(gdata))

