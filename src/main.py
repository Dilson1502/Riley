from utils.sentiments import FormatoSentimiento , Analizador , AnalizadorDeSentimientos
from utils.functions import get_user_input
from textblob import TextBlob

class FormatoSentimientoTipo1(FormatoSentimiento):
    def __init__(self,nombre_sentimiento:str,color:str) -> None:
        self.nombre_sentimiento = nombre_sentimiento
        self.color = color
    
    def __str__(self) -> str:
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre_sentimiento)

class AnalizadorTextBlob(Analizador):
    
    def polarity(self,texto):
        analisis = TextBlob(texto)
        resultado = analisis.sentiment.polarity
        return resultado

if __name__ == "__main__":
    while True:
        message = get_user_input()
        rangos = [
            ((-0.6,-0.3),FormatoSentimientoTipo1("negativo","31")),
            ((-0.3,-0.1),FormatoSentimientoTipo1("algo negativo","31")),
            ((-0.1,0.1),FormatoSentimientoTipo1("neutral","31")),
            ((0.1,0.4),FormatoSentimientoTipo1("algo positivo","32")),
            ((0.4,0.9),FormatoSentimientoTipo1("positivo","32")),
            ((0.9,1),FormatoSentimientoTipo1("muy positivo","32")),
        ]
        default_sentiment = FormatoSentimientoTipo1("extremandamente negativo",31)
        AnalizerType = AnalizadorTextBlob()   
        Polaridad = AnalizerType.polarity(message)
        SentimentAnalysisRun  = AnalizadorDeSentimientos(AnalizerType,rangos).analizar_sentimiento(message,default_sentiment)
        print(f"la polaridad de tu mensaje es: {Polaridad} y tu sentimiento es {SentimentAnalysisRun}")