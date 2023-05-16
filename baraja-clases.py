
import random
class Baraja:
    # instanciamos la clase -> inicializamos la clase con el metodo __init__ (metodo dunder) . Es el constructor
    def __init__(self, palos, numeros, limit_cart, mano, jugadores):
        self.palos = palos
        self.numeros= numeros
        self.limit_cart = limit_cart
        self.mano = mano
        self.jugadores = jugadores
            
    def crearBaraja(self,palos,numeros):
    
        naipes=[]
        naipe =[]
        numero=[]
        for i in range(len(palos)) :
            # listas de lista
            naipes.append([])
            naipe+= palos[i]
            
            for j in range(len(numeros)) :
                numero += numeros[j]
                naipes[i].append(numero[j] + naipe[i])
                
        return(naipes)

    def position_random(self,limit_cart):
        
        list_position = []
        while len(list_position) < limit_cart :
            numero = random.randint(0,43)  
            if numero not in list_position:
                list_position.append(numero)
        
        return(list_position)

    def convert_baraja(self,baraja) :
        
        baraja_convertida = []
        for item in baraja:
            baraja_convertida += item
            
        return baraja_convertida
        
    def mezclar(self,baraja):
        
        new_baraja = self.convert_baraja(baraja)
        positions = self.position_random(limit_cart)
        barajadas = []
        
        for position in positions :
            naipe = new_baraja[position]
            barajadas.append(naipe)
    
        return barajadas
    
    def repartir(self,baraja,mano,jugadores) : 
        cartas_jugadores = []
        carta= []
        if (mano*jugadores < len(baraja)):
            for i in range(jugadores) :
                cartas_jugadores.append([])
                for j in range(mano):
                    carta= baraja[j]
                    cartas_jugadores[i].append(carta) 
                    # elimino la cartas usada
                    baraja.pop(j)
                    
                    if i == jugadores : 
                        cartas_jugadores.append([])
                        
        else :
            print("No hay suficientes cartas en la baraja")
                    
        return cartas_jugadores
       
    def mostrar_cartas(self,cartas):
        carta_jugador = []
        
        for i in range(len(cartas)):
            carta_jugador = cartas[i]
            num_jugador = i + 1
            
            print(f'Jugador-{num_jugador}:{carta_jugador}')
            
        
    
palos =['o','c','e','b']
numeros=['A','1','2','3','4','5','6','7','S','C','R']
limit_cart = 44
mano = 8
jugadores = 2

baraja = Baraja(palos,numeros,limit_cart, mano,jugadores)

new_baraja = baraja.crearBaraja(palos,numeros)
baraja_mezclada = baraja.mezclar(new_baraja)
repartir = baraja.repartir(baraja_mezclada,mano,jugadores)
mostrar = baraja.mostrar_cartas(repartir)



