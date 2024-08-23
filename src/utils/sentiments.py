from textblob import TextBlob
from abc import ABC,abstractmethod


class FormatoSentimiento(ABC):
    
    @abstractmethod
    def __str__(self) -> str:
        return super().__str__()


class Analizador(ABC):
    
    @abstractmethod
    def polarity(self):
        pass
    


class AnalizadorDeSentimientos:
    
    def __init__(self,tipo_analizador,rangos) -> None:
        self.analizador = tipo_analizador
        self.rangos = rangos
   
    def analizar_sentimiento(self,texto:str,default_sentiment:FormatoSentimiento):
        for rango , sentimiento in self.rangos:
            if rango[0] < self.analizador.polarity(texto) <= rango[1]:
                return sentimiento
            else: pass
        return default_sentiment
       
