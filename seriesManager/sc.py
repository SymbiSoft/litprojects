import re,os,sys
import zipfile,os.path,shutil

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

def rename(avi,srt):
    '''avi and srt full path -> srt renamed file'''
    avidir,avifile=os.path.split(avi)
    srtdir=os.path.dirname(srt)
    temp=os.path.join(srtdir,".".join(avifile.split(".")[:-1]+["srt"]))
    os.rename(srt,temp)
    shutil.move(temp,avidir)
    return temp

def unzip(zipped):
    '''zipped fullpath -> srt files
    unzipped files in the same directory,
    purge directory and non srt file'''
    z=zipfile.ZipFile(zipped)
    zipdir=os.path.dirname(zipped)
    files=[name for name in z.namelist() if not name.endswith(os.sep) and not name.startswith("__MAC") and name.endswith(".srt")]
    for name in files:
        out=open(os.path.join(zipdir,name),"wb")
        out.write(z.read(name))
        out.close()
    return [os.path.join(zipdir,f) for f in files]
