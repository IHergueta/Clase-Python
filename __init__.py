'''
Created on 16 nov. 2020

@author: Ignacio
'''

class aula:
    def __init__(self,largo,ancho,alto,aforo_completo):
        self.__largo = largo
        self.__ancho = ancho
        self.__alto = alto
        self.__aforo_completo = aforo_completo
        
    @property
    def largo(self):
        return self.__largo

    @largo.setter
    def altura(self,largo):
        self.__largo = largo
        
    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self,ancho):
        self.__ancho = ancho
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self,alto):
        self.__alto = alto
        
    @property
    def aforo_completo(self):
        return self.__aforo_completo
    
    @aforo_completo.setter
    def aforo_completo(self,aforo_completo):
        self.__aforo_completo = aforo_completo
        
    def completo(self):
        self.__aforo_completo=True
        
    
    
    def estado(self):
        if(self.__aforo_completo == True):
            return "Esta completo el aforo de la clase"
            
        else:
            return "No esta completo el aforo"
            
  
       
  