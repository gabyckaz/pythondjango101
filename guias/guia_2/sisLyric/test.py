from Modelos import Artista
from Modelos import Album
from Modelos import Cancion
from Modelos import cargarModelos

art = Artista()
art.nombre = "HELLOWEEN"
art.nacionalidad = "ALEMANIA"
art.canciones = []
art.save()

alb = Album()
alb.titulo = "MY GOD GIVEN RIGHT"
alb.artistas = [art.getId()]
alb.anio=2015
alb.save()

can = Cancion()
can.titulo = "BATTLE'S WON"
can.album = alb.getId()
can.genero = "POWER METAL"
can.lirica= None
can.save()

print(cargarModelos())