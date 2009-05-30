#   This file is part of emesene.
#
#    Eval plugin is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    Eval plugin is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with emesene; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

VERSION = '0.2'
import Plugin
import serial
import gobject



class MainClass(Plugin.Plugin):
    '''Main plugin class'''
    def __init__(self, controller, msn):
        '''Contructor'''
        Plugin.Plugin.__init__(self, controller, msn)
        
        self.description = _('Hardware notification')
        self.authors = { 'ilich' : 'ilich.ramirez gmail'}
        self.website = ''
        self.displayName = _('HDnot')
        self.name = 'HDnot'
        self.controller = controller

        self.config = self.controller.config
        self.config.readPluginConfig(self.name)
        self.timeout = 0
        self.enabled = False
	self.period = 1000
        self.read_config()


    def start(self):
        '''start the plugin'''
	self.newMsgId = self.connect('message-received', self.newMsg)
        self.offMsgId = self.connect('offline-message-received', self.newMsg)
	self.statusChanged = self.connect('self-status-changed', self.selfStatusChanged)
	self.ser=serial.Serial(self.address, 9600,timeout=0)
	gobject.source_remove(self.timeout)
	self.timeout = gobject.timeout_add(self.period, self.refresh)
        self.enabled = True
	self.ser.flushInput()
	self.changed=True
    
    def refresh(self):
	c=self.ser.read(1)
	if c and not self.changed:
		self.disconnect(self.statusChanged)
		if c =='F':
			self.controller.contacts.set_status('NLN')
			print "Libero"
		if c =='B':
			self.controller.contacts.set_status('AWY')
			print "Occupato"
		self.ser.flushInput()
		self.changed=True
		self.statusChanged = self.connect('self-status-changed', self.selfStatusChanged)
	else:
		self.changed=False
	return True
    
    def selfStatusChanged(self, msnp, status):
	if status in ['LUN','PHN','BRB','AWY','HDN','IDL','FLN'] and not self.changed:
		self.ser.write("B")
	else:
		self.ser.write("F")

    def newMsg(self, msnp, email):
        '''called when someone send a message'''

	result = self.controller.conversationManager.getOpenConversation(email)
        if result != None:
            #if self.notifyStarted:
            #    return
            window, conversation = result
            windowFocus = window.is_active()
            tabFocus = (window.conversation == conversation)
            if windowFocus and tabFocus:
                return
	self.ser.write("H")
	
    def stop(self):    
        '''stop the plugin'''
        self.disconnect(self.newMsgId)
	self.disconnect(self.offMsgId)
	self.disconnect(self.statusChanged)
	self.enabled = False
	


    def check(self):
        return (True, 'Ok')

    
    def configure(self):
        '''Configuration Dialog'''
        l=[]
        l.append(Plugin.Option('serial', str, _('Serial (es: /dev/ttyUSB0):'), '', 
                 self.config.getPluginValue( self.name, 'serial', '' )))
        
        response = Plugin.ConfigWindow(_('HDnot Configuration'), l).run()
        if response:
            self.address = response['serial'].value
            self.write_config()
            self.start()
        return True
    
    def write_config(self):
        '''save the plugin config'''
        self.config.setPluginValue(self.name, 'serial', str(self.address))

    def read_config(self):
        '''read the plugin values'''
        self.address = self.config.getPluginValue(self.name, 'serial', '/dev/ttyUSB0):')

