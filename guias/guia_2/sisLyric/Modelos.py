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
        pass

MODELOS = {}

def persistirModelos():
        pass

def getNextId():
    if len(MODELOS.keys())==0: return 1
    else: return max(MODELOS.keys())+1

class Modelo:
    __id = None
    __cname = None
        
    @classmethod
    def get(cls, sid):
        pass
    
    @classmethod
    def getAll(cls):
        pass
        
    def getId(self):
        return self.__id
    
    def save(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
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
    