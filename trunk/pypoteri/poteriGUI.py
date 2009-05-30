from poteri import ORM
ORM.set_db_path(u"c:\\Data\\python\\poteri.db")
from poteri.model import Poteri

import appuifw
import e32
import e32dbm

enum={}
enum["azione"]=[u"Standard",u"Minore",u"Movimento"]
enum["tipo"]=[u"Incontro",u"Volonta'",u"Giornaliero",u"Utilita'"]

attacco=e32dbm.open(u"c:\\Data\\python\\attacchi.db","c")

def potere(id):
	def x():
		p=Poteri.select(where=u"id="+unicode(id)).next().dict()
		s=""
		for k,v in p.items():
			if k in enum.keys():
				v=enum[k][int(v)]
			if k=="attacco" and str(v) in [a for a in attacco.iterkeys()]:
				v=attacco[str(v)]
			s+="%s: %s\n" %(k.title(), str(v))
		round.set(unicode(s))
	return x

def elenca():
	s="ID\tNome\n"
	for p in Poteri.select():
		s+="%d\t%s\n"%(p.id,p.nome)
	round.set(unicode(s))

def usa_potere():
	id=appuifw.query(u"Id potere da usare","number")
	p=Poteri.select(where=u"id="+unicode(id)).next()
	if p.usato==1:
		appuifw.note(u"Potere gia' utilizzato","error")
	elif p.tipo==2:
		appuifw.note(u"Potere a volonta'","info")
	else:
		p.usato=1
		appuifw.note(u"%s utilizzato" % p.nome,"info")

def edit_value(d, key):
	def x():
		p=Poteri.select(where=u"id="+unicode(d["id"])).next()
		r=0
		if key in enum.keys():
			r=appuifw.selection_list(choices=enum[key], search_field=0)
		elif key=="attacco":
			round.set(unicode([a for a in attacco.iteritems()]))
			ri=appuifw.selection_list(choices=[unicode(a) for a in attacco.itervalues()]+[u"aggiungi"], search_field=1)
			if ri==len(attacco):
				#round.set(unicode([a for a in attacco]))
				i=len(attacco)
				attacco[str(i)]=appuifw.query(u"Nuovo tipo di attacco","text")
				r=i
			else:
				r=ri
		else:	
			r=appuifw.query(u"Nuovo valore","text")
		if r:
			p[key]=r
		#back()
	return x

def edit_potere(d):
	def x():
		round.set(u"Scegli valore da modificare")
		edit_menu=[(u"Indietro",back)]+[(unicode(k.title()),edit_value(d,k)) for k in d.keys()]
		appuifw.app.menu=edit_menu
	return x	
		
def back():
	round.set(u'press options')
	refresh()
	
def reset_poteri_giornalieri():
	for p in Poteri.select():
		p.usato=0
	appuifw.note(u"Reset poteri giornalieri","info")
	
def reset_poteri_incontro():
	for p in Poteri.select(where=u"tipo=2"):
		p.usato=0
	appuifw.note(u"Reset poteri a incontro","info")
	
def exit_key_handler():
    app_lock.signal()
 
def refresh():
	appuifw.app.menu= [(u"Elenca Poteri", elenca),
					(u"Usa potere",usa_potere),
					(u"Reset",((u"Incontro",reset_poteri_incontro),(u"Giornalieri",reset_poteri_giornalieri))),
					(unicode(enum["tipo"][1]),tuple([(p.nome,potere(p.id)) for p in Poteri.select(where=u"tipo=1")])),
					(unicode(enum["tipo"][0]),tuple([(unicode(p.nome),potere(p.id)) for p in Poteri.select(where=u"tipo=0")])),
					(unicode(enum["tipo"][2]),tuple([(unicode(p.nome),potere(p.id)) for p in Poteri.select(where=u"tipo=2")])),
					(u"Tutti",tuple([(unicode(p.nome),potere(p.id)) for p in Poteri.select()])),
					(u"Edit",tuple([(unicode(p.nome),edit_potere(p.dict())) for p in Poteri.select()])),
					(u"Refresh menu",refresh)]
# create the callback functions for the application menu and its submenus

app_lock = e32.Ao_lock()
round = appuifw.Text()
round.set(u'press options')
appuifw.app.screen='large'
appuifw.app.body = round

# create the application menu including submenus
refresh()

appuifw.app.exit_key_handler = exit_key_handler
app_lock.wait()

#print 