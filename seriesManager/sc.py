import re,os,sys

TOR="/media/disk/download/torrent"
SUBS="/home/ilich/Download"

def find(r,directory):
  for f in os.listdir(directory):
    m=r.match(f)
    if m:
      yield m.group()
    

def make_pattern(serie,S,E,formato):
  s=r".*%s.*0?%s\D\D?0?%s\D.*%s" % (serie,S,E,formato)
  return re.compile(s,re.IGNORECASE)
