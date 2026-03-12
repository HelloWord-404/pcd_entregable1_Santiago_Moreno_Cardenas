from typing import List
from repuesto import Repuesto

class Almacen:
    """
    Clase que representa un almacén de repuestos.
    """

    def __init__(self, nombre: str, ubicacion: str):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.catalogo: List[Repuesto] = []

    def añadir_repuesto(self, repuesto: Repuesto):
        """
        Añade un repuesto al catálogo del almacén.
        """
        for r in self.catalogo:
            if r.nombre == repuesto.nombre:
                raise ValueError("El repuesto ya existe en el catálogo")

        self.catalogo.append(repuesto)

    def eliminar_repuesto(self, nombre: str):
        """
        Elimina un repuesto del catálogo.
        """
        for repuesto in self.catalogo:
            if repuesto.nombre == nombre:
                self.catalogo.remove(repuesto)
                return

        raise ValueError("El repuesto no existe en el catálogo")

    def buscar_repuesto(self, nombre: str) -> Repuesto:
        """
        Busca un repuesto por su nombre.
        """
        for repuesto in self.catalogo:
            if repuesto.nombre == nombre:
                return repuesto

        raise ValueError("Repuesto no encontrado")

    def actualizar_stock(self, nombre: str, cantidad: int):
        """
        Actualiza el stock de un repuesto.
        """
        repuesto = self.buscar_repuesto(nombre)

        if cantidad > 0:
            repuesto.añadir_stock(cantidad)
        else:
            repuesto.retirar_stock(abs(cantidad))

    def mostrar_catalogo(self):
        """
        Muestra todos los repuestos disponibles.
        """
        print(f"\n📦 Catálogo del almacén: {self.nombre}\n")

        if not self.catalogo:
            print("No hay repuestos disponibles")
            return

        for repuesto in self.catalogo:
            print(repuesto)

    def calcular_valor_total_inventario(self) -> float:
        """
        Calcula el valor total de todos los repuestos del almacén.
        """
        total = 0

        for repuesto in self.catalogo:
            total += repuesto.calcular_valor_total()

        return total


# ============================
# Código de prueba
# ============================

if __name__ == "__main__":

    try:

        # Crear almacén
        almacen = Almacen("Almacen Imperial", "Nebulosa Kaliida")

        # Crear repuestos
        r1 = Repuesto("Motor Hiperespacial", "Kuat Drive Yards", 10, 50000)
        r2 = Repuesto("Escudo Deflector", "Sienar Fleet Systems", 5, 75000)

        # Añadir repuestos
        almacen.añadir_repuesto(r1)
        almacen.añadir_repuesto(r2)

        # Mostrar catálogo
        almacen.mostrar_catalogo()

        # Actualizar stock
        almacen.actualizar_stock("Motor Hiperespacial", 5)

        # Retirar stock
        almacen.actualizar_stock("Escudo Deflector", -2)

        print("\nValor total inventario:", almacen.calcular_valor_total_inventario(), "€")

    except Exception as e:
        print("Error:", e)