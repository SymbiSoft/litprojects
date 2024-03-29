#!/usr/bin/python
# -*- coding: utf-8 -*-
import re,os,sys,renSubs

TOR="/dati2/download/torrent"
TOR2="/torrent"
SUBS="/home/ilich/Scaricati"

def find(r,directory):
  for f in os.listdir(directory):
    m=r.match(f)
    if m:
      yield m.group()
    

def make_pattern(serie,S,E,formato):
  s=r".*%s.*0?%s\D\D?0?%s\D.*%s" % (serie,S,E,formato)
  return re.compile(s,re.IGNORECASE)

def main(argv):
  srtfile=avifile=""
  t2=False
  if len(argv)>=5:
    serie,S,E,formato=argv[1:5]
    p=make_pattern(serie,S,E,formato)
    l=[i for i in find(p,TOR)]
    if len(l)==0:
      l=[i for i in find(p,TOR2)]
      t2=True
    if len(l)==0:
      print "avi mancante"
    elif len(l)==1:
      avifile=l[0]
    else:
      for k,v in enumerate(l):
        print k," ",v
      avifile=l[int(raw_input( "File multiplo, scegli: "))]
        
    p=make_pattern(serie,S,E,"zip")
    l=[i for i in find(p,SUBS)]
    if len(l)==0:
      print "File zip mancante"
    elif len(l)==1:
      srtfile=l[0]
    else:
      for k,v in enumerate(l):
        print k," ",v
      srtfile=l[int(raw_input( "File multiplo, scegli: "))]
    if srtfile and avifile:
      if not t2:
	print TOR+"/"+avifile
      else:
	print TOR+"/"+avifile
      print SUBS+"/"+srtfile
      if not t2:
	sysargv=["scopritore",TOR+"/"+avifile,SUBS+"/"+srtfile]+argv[5:]
      else:
	sysargv=["scopritore",TOR2+"/"+avifile,SUBS+"/"+srtfile]+argv[5:]
      renSubs.main(sysargv)
  else:
    print "errore argomenti"

if __name__=="__main__":
  main(sys.argv)
