# -*- coding: utf-8 -*-
"""
@author: lennin

Clase base Modelo

Sera heredada por los otros modelos, se implementan las operaciones necesarias
para la persistencia de los datos, ninguna clase que lo herede en ningun motivo
debe editar las variables __id y __cname, porque provocara una posible falla 
en el sistema de persistencia
"""
# import pickle
import os

ARCHIVO_PERSISTENCIA = 'db'
ARCHIVO_PERSISTENCIA_LCK = 'db.lck'

def cargarModelos():
    pass

MODELOS = cargarModelos()

def persistirModelos():
    pass

def getNextId():
    if len(MODELOS.keys())==0: return 1
    else: return max(MODELOS.keys())+1

class Modelo:
    """
        Clase base, para este ejercicio se tendran 2 metodos de clase 
        (get y getAll) que seran decorados con la anotacion @classmethod
        los demas metodos seran normales y no se ocupara de esa anotacion 
        (por ejemplo __repr__)
    """
    __id = None
    __cname = None
        
    @classmethod
    def get(cls, sid):
        pass
    
    @classmethod
    def getAll(cls):
        pass

    def __repr__(self):
        return "<class %s id: %s>"%(self.__cname,self.__id)



if __name__=="__main__":
    print (MODELOS)
    class Persona(Modelo):
        nombre = None
        estadoCivil = None
        
        def __repr__(self):
            return "<objeto %s id: %s nombre: %s, apellido %s>" %('Persona',
                                self.getId(), self.nombre, self.estadoCivil)
    
    p = Persona()
    p.nombre = 'Juan Perez'
    p.estadoCivil = 'Soltero'
    p.save()
    
    p = Persona()
    p.nombre = 'Juan Perez'
    p.estadoCivil = 'Soltero'
    p.save()
    
    print(MODELOS)
    print(Persona.get(p.getId()))
    print(Persona.getAll())
        
        
        