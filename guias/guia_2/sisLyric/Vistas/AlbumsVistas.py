
from Controladores import AlbumControlador

from Vistas.BaseVista import VistaBase, entrada, salir

from Modelos import Album

def consultar_todos():
    print("ALBUMS: ")
    print(AlbumControlador.get_all_albums())

def consultar_por_id():
    aid = entrada("ID A BUSCAR: ")
    a = AlbumControlador.get_album_by_id(aid)
    print("ALBUM: ")
    print(a)

def consultar_por_similares():
    sim = entrada("FILTRO: ")
    a = AlbumControlador.get_album_with_similarity(sim)
    print("ALBUMS: ")
    print(a)

def agregar_album():
    a = Album()
    a.titulo = entrada("TITULO: ")
    a.artistas = entrada("ARTISTAS: (id separados por espacio)").split(" ")
    a.anio = entrada("ANIO: ")
    AlbumControlador.save_album(a)
    print("ARTISTA AGREGADO (id %d)"%(a.getId()))

class VistaAlbum(VistaBase):
    menu = {
        1: ("CONSULTAR TODOS LOS ALBUMS", consultar_todos),
        2: ("BUSCAR ALBUM POR ID", consultar_por_id),
        3: ("BUSCAR POR SIMILITUD", consultar_por_similares),
        4: ("AGREGAR", agregar_album),
        5: ("salir", salir)
    }
    