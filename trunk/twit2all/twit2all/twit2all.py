# -*- coding: utf-8 -*-
import twitter
import re
import commands
import sys,os

class  twit2all(object):
  def __init__(self):
    self.last_id=None
    self.cron_line=None
    self.time=None
    self.path=os.path.join(os.getcwd(),os.path.dirname(sys.argv[0]))
    self.filename=os.path.split(sys.argv[0])[1]
    self.cron_file=os.path.join(self.path, ".%s.cron" % self.filename)
    self.conf_file=os.path.join(self.path, ".%s.conf" % self.filename)

  def login_twitter(self, user=None, pwd=None):
    if "username" in self.__dict__:      
      self.api=twitter.Api(username=user, password=pwd)
      try:
        self.timeline=self.api.GetUserTimeline(self.username)
      except: raise Exception("The user %s has protected their updates."% self.username)
      self.User=self.api.GetUser(self.username)
    else:
      raise Exception("You must set a twitter username")
    
  def set_action_list(self, t):
    self.action=t
  def debug(self, count):
    self.status=self.api.GetUserTimeline(self.username)
    for regex,function in self.action:
      r=re.compile(regex)
      for s in self.status:
        m=r.match(s.GetText())
        if m:
          if hasattr(function,"__call__"):
            try:
              function(*m.groups())
            except TypeError as detail: raise Exception(detail,function.__name__, m.groups())
            else:
              print function.__name__ ,"called with arguments", m.groups()
          else:
            try:
              print function % m.groups()
            except TypeError as detail: raise Exception(detail, function, m.groups())
         
  def load_last_id(self, last_id=None):
    '''load last id from a configuration file named <file_name> if exist, else create that file. 
  If file doesn't exist and <last_id> isn't None he file is created and filled with <last_id>'''
    try:
      self.config=open(self.conf_file,"r+")
    except IOError as detail:
      if str(detail).startswith("[Errno 2]"):
        try:
          self.config=open(self.conf_file,"w+")
        except IOError as detail:
          if str(detail).startswith("[Errno 13]"):
            raise Exception("Permission denied to access %s"%file_name)
        else:
          self.last_id=last_id
    else:
      self.last_id=str(int(self.config.readline()))
  
  def run(self, last_id=None):
    self.load_last_id(last_id)
    if not "config" in self.__dict__: raise Exception("No config file found")
    self.status=self.api.GetUserTimeline(self.username, since_id=self.last_id)
    for regex,function in self.action:
      r=re.compile(regex)
      for s in self.status:
        m=r.match(s.GetText())
        if m:
          if hasattr(function,"__call__"):
            try:
              function(*m.groups())
            except TypeError as detail: raise Exception(detail,function.__name__, m.groups())
          else:
            try:
              commands.getoutput(function % m.groups())
            except TypeError as detail: raise Exception(detail, function, m.groups())
    if self.status:
      self.last_id=str(self.status[0].id)
      self.config.seek(0)
      self.config.write(self.last_id)
      self.config.close()
  
  def set_cron(self, m=60):
    '''twitter will be checked every <m> minutes'''
    self.cron_line="*/%d * * * * " % m
    self.cron_line+=os.getenv('USER')
    self.cron_line+=" python %s --run" % (os.path.join(self.path,self.filename))
    
  def help(self):
    print "help"
  
  def cron(self):
    if self.time: 
      self.set_cron(self.time)
      fh = open(self.cron_file,"w+")
      fh.write(self.cron_line+"\n")
      fh.close()
      commands.getoutput("crontab %s" % self.cron_file)
    else:
      raise Exception("No frequency time found")
  
  def start(self):
    if len(sys.argv)==1:
      self.help()
    elif len(sys.argv)==2:
      if sys.argv[1]=='--help':
        self.help()
      elif sys.argv[1]=='--run':
        self.run()
      elif sys.argv[1]=='--cron':
        self.cron()
      else:
        self.help()