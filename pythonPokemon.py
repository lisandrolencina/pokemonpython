import time
import numpy as np
import sys

#Imprimir con demora

def imprimirConRetraso(s):
    #Imprimir una letra a la vez
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#Crear la clase

def __init__(self, nombre, tipos, movimientos, EVs, puntosDeSalud = '==============='):

    #Guardar las variables como atributos
    self.nombre = nombre
    self.tipos = tipos
    self.movimientos = movimientos
    self.ataque = EVs['ataque']
    self.defensa = EVs['defensa']
    self.puntosDeSalud = puntosDeSalud
    self.barras = 20 # puntosDeSalud
  

    #Clase de Pokemon2
def impresa(self,Pokemon2):

  '''Imprimir informacion de lucha ''' 

  print(" BATALLA POKEMON!")
  
  #Pokemon1
  print(f"\n{self.nombre}")
  print("tipo/", self.tipos)
  print("ataque/", self.ataque)
  print("defensa/", self.defensa)
    #promedio de ataque y la defensa
  print("Nv./", 3*(1+np.mean([self.ataque,self.defensa])))
  
  print("\nVS")

  #Pokemon2
  print(f"\n{Pokemon2.nombre}")
  print("tipo/", Pokemon2.tipos)
  print("ataque/", Pokemon2.ataque)
  print("defensa/", Pokemon2.defensa)
    #promedio de ataque y la defensa
  print("Nv./", 3*(1+np.mean([Pokemon2.ataque,Pokemon2.defensa])))
  
  #El timesleep va a demorar el siguiente codigo por 2 Segundos
  time.sleep(2)




  #Ventaja de pokemones

  '''
    Considera la ventaja de tipo 
    Actualiza poderes de ataque y defensa
    Devuelve dos cadenas de informacion 

  '''


  version = ['fuego', 'agua', 'planta']
  for i,k in enumerate(version):
        if self.tipos == k:
            #Son el mismo tipo
            if Pokemon2.tipos == k:
                cadena1Ataque = '\nNo es muy efectivo...'
                cadena2Ataque = '\nNo es muy efectivo...'

    #Pokemon2 Tiene ventaja
        if Pokemon2.tipos == version [(i+1)%3]:
            Pokemon2.ataque *= 2
            Pokemon2.defensa *= 2
            self.ataque /= 2
            self.defensa /= 2
            cadena1Ataque = '\nNo es muy efectivo...'
            cadena2Ataque = '\nEs muy eficaz!...'

               #Pokemon2 Tiene desventaja
        if Pokemon2.tipos == version [(i+2)%3]:
            self.ataque *= 2
            self.defensa *= 2
            Pokemon2.ataque /= 2
            Pokemon2.defensa /= 2
            cadena1Ataque = '\nEs muy efectivo...'
            cadena2Ataque = '\nVas a perder...'

        return cadena1Ataque, cadena2Ataque
            

    

        def turno(self, Pokemon2, cadena1Ataque, cadena2Ataque):

          while (self.barras > 0 ) and (Pokemon2.barras > 0):

            #imprimor puntos salud de cada pokemon
            print(f"\n{self.nombre}\t\tPS\t{self.puntosDeSalud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntosDeSalud}")

        #POKEMON 1
        print(f"Adelante! {self.nombre}!")
        for i, x in enumerate(self.movimientos):
            print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            imprimirConRetraso(f"{self.nombre} uso {self.movimientos[index-1]}")
            time.sleep(1)
            imprimirConRetraso(cadena1Ataque)

            # Determinar el daño
            Pokemon2.barras -= self.ataque
            Pokemon.puntosDeSalud= ""

            #Agregar barras adicionales
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.puntosDeSalud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntosDeSalud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntosDeSalud}")
            time.sleep(.5)

            #comprobar si pokemon se debilito 

            if Pokemon2.barras <= 0:
                imprimirConRetraso("\n..." + Pokemon2.nombre + 'se debilito.')
                break


            
        #POKEMON 2
        print(f"Adelante! {Pokemon2.nombre}!")
        for i, x in enumerate(Pokemon2.movimientos):
            print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            imprimirConRetraso(f"{Pokemon2.nombre} uso {Pokemon2.movimientos[index-1]}")
            time.sleep(1)
            imprimirConRetraso(cadena1Ataque)

            # Determinar el daño
            self.barras -= Pokemon2.ataque
            Pokemon.puntosDeSalud= ""

            #Agregar barras adicionales
            for j in range(int(self.barras+.1*self.defensa)):
                self.puntosDeSalud += "="

            time.sleep(1)
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntosDeSalud}")
            print(f"\n{self.nombre}\t\tPS\t{self.puntosDeSalud}")
            time.sleep(.5)

            #comprobar si pokemon se debilito 

            if self.barras <= 0:
                imprimirConRetraso("Pokemon2..." + self.nombre + 'se debilito.')
                break

            def lucha (self,Pokemon2):
                #permite que los pokemones luchen entre ellos
                self.impresa(Pokemon2)


                cadena1Ataque, cadena2Ataque = self.ventaja(Pokemon2)

                #lucha real
                #la lucha continua hasta que uno no tenga vida
                self.turno(Pokemon2, cadena1Ataque, cadena2Ataque)

                #premio
                money = np.random.choice(5000)
                imprimirConRetraso(f"\nEl oponente te pago ${money}.\n")
            if __nombre__ == '__main__':
                #crear objeto
                Charizard = Pokemon('Charizard','fuego',['Lanzallamadas','pirotecnia','Giro de fuego','Ascuas',{'ataque':12, 'defensa': 8}])
                Blastoise = Pokemon('Blastoise','agua',['Pistola de agua','burbuja','Hidro pulso','Hidro Bomba',{'ataque':10, 'defensa': 10}])
                Venusaur = Pokemon('Venusaur','planta',['Lati cepa','Hoja afialada','Rayo solar','Abatidoras',{'ataque':8, 'defensa': 12}])