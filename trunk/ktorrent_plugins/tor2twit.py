#!/usr/bin/env kross
# -*- coding: utf-8 -*-


import Kross
#from twyt import twitter
import logging
logger = logging.getLogger('tor2twit')
hdlr = logging.FileHandler('/home/ilich/.ktorrent/script.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

import time
import os
import KTorrent
import KTScriptingPlugin
import commands
logger.info("Start script2")
class tor2twit:
        def __init__(self):
		self.user = "azurill"
		self.pwd = "R4mirez!"
		#self.t=twitter.Twitter()
                #self.t.set_auth(self.user,self.pwd)
		KTorrent.connect("torrentAdded(const QString &)",self.torrentAdded)
		tors = KTorrent.torrents()
		#logger.info("Log on twitter")
		# bind to signals for each torrent
		for t in tors:
			self.torrentAdded(t)

	#def twit(self,text):
		#try:
                        #self.t.status_update(text)
		#except:
                        #self.t.set_auth(self.user,self.pwd)
                        #try:
                                #self.t.status_update(text)
                        #except:
                                #KTorrent.log("Errore nell'invio twit: ", text)
                                #logger.info("Errore nell'invio twit: "+ text)
	def twit(self,text):
		logger.info(commands.getoutput("twidge update \"%s\"" % text))
		logger.info(text)

	def save(self):
		KTScriptingPlugin.writeConfigEntry("tor2twit","username",self.user)
		KTScriptingPlugin.writeConfigEntry("tor2twit","password",self.pwd)
		KTScriptingPlugin.syncConfig("tor2twit")
	
	def load(self):
		self.user = KTScriptingPlugin.readConfigEntry("tor2twit","username",self.user)
		self.pwd = KTScriptingPlugin.readConfigEntry("tor2twit","password",self.pwd)

	def configure():
		forms = Kross.module("forms") 
		dialog = forms.createDialog("My Cool Script Settings")
		dialog.setButtons("Ok|Cancel")

	def torrentFinished(self,tor):
                self.twit("The download of the torrent " + tor.name() + " has finished!")
		
	def torrentStoppedByError(self,tor,error_message):
		self.twit("Torrent " + tor.name() + " was stopped by an error: " + error_message)
		
	def seedingAutoStopped(self,tor,reason):
		self.twit("Torrent " + tor.name() + " has finished seeding because " + reason)
		
	def corruptedDataFound(self,tor):
		self.twit("KTorrent has found corrupted data in the torrent " + tor.name())
	

	def connectSignals(self,tor):
		KTorrent.log("connectSignals " + tor.name())
		tor.connect("finished(QObject* )",self.torrentFinished)
		tor.connect("stoppedByError(QObject* ,const QString & )",self.torrentStoppedByError)
		tor.connect("seedingAutoStopped(QObject* ,const QString & )",self.seedingAutoStopped)
		tor.connect("corruptedDataFound(QObject* )",self.corruptedDataFound)
	
	def torrentAdded(self,ih):
		tor = KTorrent.torrent(ih)
		self.connectSignals(tor)
 
# load settings
notifier = tor2twit()
notifier.load()

def configure():
	global notifier
	notifier.configure()

def unload():
	global notifier
	del notifier
