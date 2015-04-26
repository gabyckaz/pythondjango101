# -*- coding: utf-8 -*-
"""
@author: lennin

Controladores Album

"""
from Modelos import Album

def get_all_albums():
    return Album.getAll()

def save_album(album):
    if isinstance(album, Album):
        album.nombre = album.nombre.lower()
        album.nacionalidad = album.nacionalidad.lower()
        album.save()

def get_album_by_id(ida):
    return Album.get(ida)

def get_album_with_similarity(sim):
    albums = []
    simi = sim.lower()
    for a in Album.getAll():
        if simi in a.titulo:
            albums.append(a)
    return albums

def get_album_by_nombre(nombre):
    albums = []
    simi = nombre.lower()
    for a in Album.getAll():
        if simi in a.nombre:
            albums.append(a)
    return albums
    


