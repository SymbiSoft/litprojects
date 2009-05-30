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
import gobject
import random
import gtk
import os.path



class MainClass(Plugin.Plugin):
    '''Main plugin class'''
    def __init__(self, controller, msn):
        '''Contructor'''
        Plugin.Plugin.__init__(self, controller, msn)
        
        self.description = _('Change message')
        self.authors = { 'ilich' : 'ilich.ramirez gmail'}
        self.website = ''
        self.displayName = _('ChangePM')
        self.name = 'ChangePM'
        self.controller = controller

        self.config = self.controller.config
        self.config.readPluginConfig(self.name)
        
        self.enabled = False


        self.timeout = 0
        random.seed()
        self.read_config()


    def start(self):
        '''start the plugin'''
        if os.path.exists(self.filePath) and self.delay.isdigit() :
            f = open("/home/ilich/.config/emesene1.0/pluginsEmesene/ChangePM.txt")
            self.msgs = f.readlines()
            f.close()
            self.lenght=len(self.msgs)
            self.enabled = True
            gobject.source_remove(self.timeout)
            self.timeout = gobject.timeout_add(int(self.delay)*1000, self.refresh)
            self.refresh()
        else:
            self.configure()
        
        

    def stop(self):    
        '''stop the plugin'''
        self.enabled = False
        gobject.source_remove(self.timeout)

    def check(self):
        return (True, 'Ok')

    def refresh(self):
        '''refresh the personal message'''
        self.controller.contacts.set_message(self.msgs[random.randint(0,self.lenght-1)])
        return True
    
    def configure(self):
        '''Configuration Dialog'''
        l=[]
        l.append(Plugin.Option('delay', str, _('Delay (second):'), '', 
                 self.config.getPluginValue( self.name, 'delay', '' )))
        l.append(Plugin.Option('filePath', str, _('Path to ChangePM.txt:'), '', 
                 self.config.getPluginValue( self.name, 'filePath', '' )))
        
        response = Plugin.ConfigWindow(_('ChangePM Configuration'), l).run()
        if response:
            self.delay = response['delay'].value
            self.filePath = response['filePath'].value
            self.write_config()
            self.start()
            #gobject.source_remove(self.timeout)
            #self.timeout = gobject.timeout_add(int(self.delay), self.refresh)
        return True
    
    def write_config(self):
        '''save the plugin config'''
        self.config.setPluginValue(self.name, 'delay', str(self.delay))
        self.config.setPluginValue(self.name, 'filePath', str(self.filePath))

    def read_config(self):
        '''read the plugin values'''
        self.delay = self.config.getPluginValue(self.name, 'delay', '60000')
        self.filePath = self.config.getPluginValue(self.name, 'filePath', '$HOME/')
