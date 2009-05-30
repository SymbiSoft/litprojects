import ORM

class Poteri(ORM.Mapper2):
	class mapping:
		nome=ORM.column(ORM.String)
		livello=ORM.column(ORM.String)
		tipo=ORM.column(ORM.Integer)
		parole_chiave=ORM.column(ORM.String)
		azione=ORM.column(ORM.Integer)
		range=ORM.column(ORM.String)
		bersaglio=ORM.column(ORM.String)
		attacco=ORM.column(ORM.Integer)
		colpito=ORM.column(ORM.String)
		effetto=ORM.column(ORM.String)
		mancato=ORM.column(ORM.String)
		progressione=ORM.column(ORM.String)
		usato=ORM.column(ORM.Integer)
		memorizzato=ORM.column(ORM.Integer)

		
		
if __name__ == "__main__":
	ORM.set_db_path(u"c:\\Data\\python\\poteri.db")
	p=Poteri(nome="Fiamma sacra", livello="3 attacco, chierico")
	for p in Poteri.select():
		print p.id, p.nome

		
'''

c=db.execute(unicode("create table Poteri (id counter, nome varchar, livello varchar, tipo tinyint, parole_chiave varchar, azione tinyint, range varchar, bersaglio varchar, attacco tinyint, colpito varchar, effetto varchar, mancato varchar, progressione varchar, usato tinyint, memorizzato tinyint)"))

'''