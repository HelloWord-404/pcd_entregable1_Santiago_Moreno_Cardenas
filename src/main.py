from almacen import Almacen
from repuesto import Repuesto
from numeracion import Ubicacion, ClaseNave
from nave_estelar import Nave_Estelar
from estacion_espacial import Estacion_espacial
from caza_estelar import Caza_Estelar

def main():
    
    almacen = Almacen("Almacen Imperial", Ubicacion.NEBULOSA_KALIIDA )

    r1 = Repuesto("Motor Hiperespacial", "Kuat Drive Yards", 10, 50000)
    r2 = Repuesto("Escudo Deflector", "Corellia Corp", 5, 20000)

    almacen.añadir_repuesto(r1)
    almacen.añadir_repuesto(r2)

    almacen.mostrar_catalogo()

    # Actualizar stock
    almacen.actualizar_stock("Motor Hiperespacial", 5)
    almacen.actualizar_stock("Escudo Deflector", -2)

    print("\nDespués de actualizar stock:")
    almacen.mostrar_catalogo()

    print("\nValor total inventario:", almacen.calcular_valor_total_inventario())

    
    nave = Nave_Estelar(100, 300, ClaseNave.EJECUTOR)
    nave.mostrar_info()
    print("Capacidad total:", nave.capacidad_total())


    estacion = Estacion_espacial(50, 200, Ubicacion.ENDOR)
    estacion.mostrar_info()

    estacion.mover_estacion(Ubicacion.NEBULOSA_KALIIDA)
    print("Después de mover:")
    estacion.mostrar_info()

    caza = Caza_Estelar(120, False)
    caza.mostrar_info()

    resultado = caza.iniciar_ataque(Ubicacion.CUMULO_RAIMOS)
    print("Resultado del ataque:", resultado)


if __name__ == "__main__":
    main()