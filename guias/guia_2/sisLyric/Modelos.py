# -*- coding: utf-8 -*-
"""
@author: lennin

Clase base Modelo

Sera heredada por los otros modelos, se implementan las operaciones necesarias
para la persistencia de los datos, ninguna clase que lo herede en ningun motivo
debe editar las variables __id y __cname, porque provocara una posible falla 
en el sistema de persistencia
"""
import pickle, os

ARCHIVO_PERSISTENCIA = 'db'
ARCHIVO_PERSISTENCIA_LCK = 'db.lck'

def cargarModelos():
    with open(ARCHIVO_PERSISTENCIA, 'rb') as pd:
        data = picke.load(pd)
    return data
    

MODELOS = {}

def persistirModelos():
    global MODELOS
    with open(ARCHIVO_PERSISTENCIA, 'wb') as pd:
        pickle.dump(MODELOS, pd)

def getNextId():
    if len(MODELOS.keys())==0: return 1
    else: return max(MODELOS.keys())+1

class Modelo:
    __id = None
    __cname = None
        
    @classmethod
    def get(cls, sid):
        global MODELOS
        MODELOS = cargarModelos()
        return MODELOS[sid]
    
    @classmethod
    def getAll(cls):
        global MODELOS
        MODELOS = cargarModelos()
        l = []
        for mid in MODELOS:
            ob = MODELOS[mid]
            if ob.__cname==cls.__name__:
                l.append(ob)
        return l
    
    def getId(self):
        return self.__id
    
    def save(self):
        global MODELOS
        MODELOS = cargarModelos()
        self.__id = getNextId()
        self.__cname = self.__class__.__name__
        MODELOS[self.__id] = self
        persistirModelos()
    
    def update(self):
        global MODELOS
        MODELOS = cargarModelos()
        MODELOS[self.__id] = self
        persistirModelos()
    
    def delete(self):
        global MODELOS
        MODELOS = cargarModelos()
        del MODELOS[self.__id]
        persistirModelos()
        
    
    def __repr__(self):
        return "<class %s id: %s>"%(self.__cname,self.__id)

class Album(Modelo):
    titulo = None
    artistas = None
    anio = None
    
class Artista(Modelo):
    nombre = None
    nacionalidad = None
    canciones = []
    
class Cancion(Modelo):
    titulo = None
    album = None
    genero = None
    lirica= None
    