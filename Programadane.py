import matplotlib.pyplot as plt


afirmacion = True
Menu = """
|--------------------------------------------|
|           Proyección Poblacional           |
|--------------------------------------------|
|                                            |
|         1. Proyección                      |
|         2. Graficar                        |
|         3. Salir                           |
|                                            |
|--------------------------------------------|
"""

datos = [
    [2018, 7830, 6420, 4840],
    [2019, 7900, 6480, 4900],
    [2020, 7970, 6535, 4955],
    [2021, 8050, 6590, 5020],
    [2022, 8120, 6645, 5090]
]
ciudades = ["Bogotá", "Antioquia", "Valle del Cauca"]

def mostrar_menu():
    print(Menu)

def proyeccion_poblacion():
    print("Proyección poblacional para los próximos 5 años:")
    for i, ciudad in enumerate(ciudades):
        pinicial = datos[0][i+1]
        pfinal = datos[-1][i+1]
        n = len(datos)-1
        tasa = (pfinal/pinicial)**(1/n) - 1
        poblacion = pfinal
        print(f"\n{ciudad}:")
        for año in range(2023, 2028):
            poblacion *= (1 + tasa)
            print(f"Año {año}: {int(poblacion)} mil habitantes")

def graficar_poblacion():
    años = [fila[0] for fila in datos]
    plt.figure(figsize=(10,6))
    for i, ciudad in enumerate(ciudades):
        poblaciones = [fila[i+1] for fila in datos]
        plt.plot(años, poblaciones, marker='o', label=ciudad)
    plt.title("Población Histórica (2018-2022)")
    plt.xlabel("Año")
    plt.ylabel("Población (mil habitantes)")
    plt.legend()
    plt.grid(True)
    plt.show()

while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if not opcion:
        print("Por favor ingrese una opción.")
    elif opcion == "1":
        proyeccion_poblacion()
    elif opcion == "2":
        graficar_poblacion()
    elif opcion == "3":
        print("Fin del programa.")
        afirmacion = False
    else:
        print("Opción inválida.") 
    




