import random
class Baraja :
    #
    def __init__(self, numeros, palos):
        self.naipes= []
        for palo in palos:
            for numero in numeros:
                naipe = numero + palo
                self.naipes.append(naipe)


    def barajar(self) : 
        for i in range(len(self.naipes)):
            j= random.randrange(len(self.naipes))
            self.naipes[i], self.naipes[j] = self.naipes[j], self.naipes[i]
            

    def repartir(self, mano, jugadores):
        players = []
        for p in range(jugadores) :
            players.append([])
        
        for num_carta in range(mano) :
            
            for jugador in range(jugadores):
                carta =  self.naipes.pop(0)
                players[jugador].append(carta)
                
        return players    