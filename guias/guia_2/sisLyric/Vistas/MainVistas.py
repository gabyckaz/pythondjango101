# -*- coding: utf-8 -*-

"""
@author: lennin

Controladores Cancion

"""


from Vistas.BaseVista import VistaBase, entrada, salir

from Vistas.AlbumsVistas import VistaAlbum

def gestionarArtistas():
    pass

def gestionarAlbums():
    VistaAlbum()

def gestionarCanciones():
    pass

class VistaMain(VistaBase):
    menu = {
        1: ("GESTION ARTISTAS", gestionarArtistas),
        2: ("GESTION ALBUMS", gestionarAlbums),
        3: ("GESTION DE CANCIONES", gestionarCanciones),
        4: ("SALIR", salir)
    }

