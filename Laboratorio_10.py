import csv

# Clase para representar el grafo usando listas de adyacencia
class Grafo:
    def __init__(self):
        self.grafo = {}

    # Método para agregar una arista entre dos ciudades
    def agregar_arista(self, ciudad_a, ciudad_b, distancia, tiempo):
        if ciudad_a not in self.grafo:
            self.grafo[ciudad_a] = []
        if ciudad_b not in self.grafo:
            self.grafo[ciudad_b] = []
        # Agregar las conexiones para ambas ciudades
        self.grafo[ciudad_a].append((ciudad_b, distancia, tiempo))
        self.grafo[ciudad_b].append((ciudad_a, distancia, tiempo))

    # Constructor del grafo con el archivo csv
    def cargar_datos(self, archivo):
        with open(archivo, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Omitir la primera fila si es una cabecera
            for row in reader:
                ciudad_a, ciudad_b, distancia, tiempo = row
                # Asegurarse de que 'distancia' y 'tiempo' sean numéricos
                try:
                    distancia = float(distancia)
                    tiempo = float(tiempo)
                    self.agregar_arista(ciudad_a, ciudad_b, distancia, tiempo)
                except ValueError:
                    print(f"Error al convertir los valores de distancia o tiempo en la fila: {row}")

    # Verificar si están conectados por una único camino
    def estan_conectadas(self, ciudad_a, ciudad_b):
        if ciudad_a in self.grafo:
            for vecino in self.grafo[ciudad_a]:
                if vecino[0] == ciudad_b:
                    return True
        return False

# Función principal para ejecutar el programa para el usuario
def main():
    grafo = Grafo()
    grafo.cargar_datos('Datos vias Colombia.csv')

    while True:
        print("\nSeleccione una opción:")
        print("1. Verificar si dos ciudades están conectadas por una única carretera")
        print("2. Salir")
        
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            ciudad_a = input("Ingrese la ciudad A: ")
            ciudad_b = input("Ingrese la ciudad B: ")
            if grafo.estan_conectadas(ciudad_a, ciudad_b):
                print(f"{ciudad_a} y {ciudad_b} están conectadas por una única carretera.")
            else:
                print(f"{ciudad_a} y {ciudad_b} NO están conectadas por una única carretera.")
        elif opcion == '2':
            break

if __name__ == "__main__":
    main()
