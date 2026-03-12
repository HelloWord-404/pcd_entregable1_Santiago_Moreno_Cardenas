import random
from numeracion import Ubicacion

class Caza_Espacial:
    def __init__(self, dotacion: int, estado_ataque: bool):
        self.__dotacion = dotacion
        self.estado_ataque = estado_ataque
        
      
    def mostrar_info(self):
        print(self)

    def isPossible_Star_Attack(self, ubicacionAtaque: Ubicacion) -> bool:
      if(self.__dotacion >100 && ubicacionAtaque != Uubicacion.ENDOR)
        return True
      else
        valor = random.choice([True, False])
        return valor
        
    def iniciar_ataque(self, ubicacionAtaque: Ubicacion) -> str:
        if(self.isPossible_Star_Attack())
          self.estado_ataque = True
        else
         self.estado_ataque = False
        if(estado_ataque) return( print("El ataque fue exitoso"))
      
    
    def __str__(self):
        return f" -> {self.estado_ataque} --> "
