import random


class CentroComercial:
    def __init__(self, inventario_inicial, tasa_reposicion):
        self.inventario = inventario_inicial
        self.tasa_reposicion = tasa_reposicion

    def llegada_clientes(self, numero_clientes):
        for _ in range(numero_clientes):
            probabilidad_compra = random.random()  # Genera un número aleatorio entre 0 y 1
            if probabilidad_compra < 0.7:  # Supongamos que el 70% de los clientes compra
                # Elige un producto aleatorio del inventario
                producto = random.choice(list(self.inventario.keys()))
                if self.inventario[producto] > 0:  # Si hay stock disponible
                    # Reduce el stock del producto en 1
                    self.inventario[producto] -= 1
                    print(f"Cliente compró {
                          producto}. Stock restante: {self.inventario}")
                else:
                    print(f"Cliente quería comprar {
                          producto}, pero no hay stock disponible.")
            else:
                print("Cliente no realizó ninguna compra.")

    def actualizar_inventario(self):
        for producto in self.inventario:
            # Incrementa el inventario según la tasa de reposición
            self.inventario[producto] += self.tasa_reposicion


def simular_abasto(duracion_simulacion, tasa_reposicion):
    inventario_inicial = {
        "pan": 50,
        "leche": 30,
        "huevos": 20
    }
    centro_comercial = CentroComercial(inventario_inicial, tasa_reposicion)

    for tiempo in range(duracion_simulacion):
        print(f"Entrada al supermercado: {tiempo}")
        # Simula la llegada de clientes
        centro_comercial.llegada_clientes(random.randint(5, 15))
        centro_comercial.actualizar_inventario()  # Simula la reposición de inventario


simular_abasto(duracion_simulacion=10, tasa_reposicion=5)
