
import random
class Baraja:
    # instanciamos la clase -> inicializamos la clase con el metodo __init__ (metodo dunder) . Es el constructor
    def __init__(self):
        self.palos = []
        self.numeros= []
        self.limit_cart = 0
        self.mano = 0
        self.jugadores = 0
        self.state = 0
            
    def crearBaraja(self):
    
        naipes=[]
        naipe =[]
        numero=[]
        for i in range(len(self.palos)) :
            # listas de lista
            naipes.append([])
            naipe += self.palos[i]
            
            for j in range(len(self.numeros)) :
                numero += self.numeros[j]
                naipes[i].append(numero[j] + naipe[i])
                
        return(naipes)

    def position_random(self):
        
        list_position = []
        limit_cart = self.calculate_carts()
        while len(list_position) < limit_cart :
            numero = random.randint(0,limit_cart - 1)  
            if numero not in list_position:
                list_position.append(numero)
        
        return(list_position)
    
    def calculate_carts(self):
        limit_cart = len(self.palos) * len(self.numeros)
        return limit_cart

    def convert_baraja(self,baraja) :
        
        baraja_convertida = []
        for item in baraja:
            baraja_convertida += item
            
        return baraja_convertida
        
    def mezclar(self,baraja):
        
        new_baraja = self.convert_baraja(baraja)
        positions = self.position_random()
        barajadas = []
        
        for position in positions :
            naipe = new_baraja[position]
            barajadas.append(naipe)
        self.state = len(barajadas)
        return barajadas
    
    def repartir(self,baraja) : 
        cartas_jugadores = []
        carta= []
        if (self.mano * self.jugadores < self.state):
            for i in range(self.jugadores) :
                cartas_jugadores.append([])
                for j in range(self.mano):
                    carta = baraja[j]
                    cartas_jugadores[i].append(carta) 
                    # elimino la cartas usada
                    baraja.pop(j)
                    self.state -= 1 
                    
                    
                    if i == self.jugadores : 
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
            
        
baraja = Baraja()
    
baraja.palos =['t','d','p','c'] 
baraja.numeros=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
baraja.mano = 4
baraja.jugadores = 4


new_baraja = baraja.crearBaraja()
baraja_mezclada = baraja.mezclar(new_baraja)
repartir = baraja.repartir(baraja_mezclada)
mostrar = baraja.mostrar_cartas(repartir)
repartir = baraja.repartir(baraja_mezclada)
mostrar = baraja.mostrar_cartas(repartir) 
repartir = baraja.repartir(baraja_mezclada)
mostrar = baraja.mostrar_cartas(repartir) 

repartir = baraja.repartir(baraja_mezclada)
mostrar = baraja.mostrar_cartas(repartir) 




