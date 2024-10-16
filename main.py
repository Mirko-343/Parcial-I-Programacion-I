# Mirko Becker

# IMPORTANTE: hay algunos prints que se exceden de la cantidad de caracteres por línea pero es porque si los acomodaba
# con enter para que entraran en la pantalla me daba un error que no tengo conocimiento de cómo solucionar.
from paquete import funciones

matriz_existencias = funciones.inicializar_matriz(7, 6, 0)

matriz_existencias = funciones.completar_matriz_existencias(matriz_existencias)

# Punto 1 listo
existencias_pba = [60000, 2500, 300, 750, 999, 800]
funciones.cargar_existencias(matriz_existencias, "PBA", existencias_pba)

existencias_caba = [500, 555, 780, 654, 200, 801]
funciones.cargar_existencias(matriz_existencias, "CABA", existencias_caba)

existencias_chubut = [555, 750, 50000, 1200, 2000, 300]
funciones.cargar_existencias(matriz_existencias, "Chubut", existencias_chubut)

existencias_tucu = [476, 4760, 220, 5478, 52, 302]
funciones.cargar_existencias(matriz_existencias, "Tucumán", existencias_tucu)

existencias_mend = [2000, 50375, 1, 2000, 1200, 814]
funciones.cargar_existencias(matriz_existencias, "Mendoza", existencias_mend)

# Punto 2 listo
print("Punto 2")
total_existencias_pba = funciones.calcular_total_existencias(matriz_existencias, "PBA")
print(f"Total de existencias depósito PBA: {total_existencias_pba}")

total_existencias_caba = funciones.calcular_total_existencias(matriz_existencias, "CABA")
print(f"Total de existencias depósito CABA: {total_existencias_caba}")

total_existencias_chubut = funciones.calcular_total_existencias(matriz_existencias, "Chubut")
print(f"Total de existencias depósito Chubut: {total_existencias_chubut}")

total_existencias_tucu = funciones.calcular_total_existencias(matriz_existencias, "Tucumán")
print(f"Total de existencias depósito Tucumán: {total_existencias_tucu}")

total_existencias_mend = funciones.calcular_total_existencias(matriz_existencias, "Mendoza")
print(f"Total de existencias depósito Mendoza: {total_existencias_mend}")

# Punto 3 listo
print("\nPunto 3")
funciones.detectar_escacez(matriz_existencias, 500)

# Punto 4 listo
print("\nPunto 4")
funciones.calcular_mayor_existencia(matriz_existencias)

# Punto 5 listo
print("\nPunto 5")
lista_valores = [5000, 3500, 4000, 1500, 500, 800]

matriz_recaudaciones = funciones.inicializar_matriz(2, 6, 0)
matriz_recaudaciones = funciones.completar_matriz_recaudaciones(matriz_recaudaciones)


recaudacion_pba = [funciones.calcular_recaudacion_deposito(matriz_existencias, lista_valores, "PBA")]
matriz_recaudaciones[1][1] = recaudacion_pba
recaudacion_caba = [funciones.calcular_recaudacion_deposito(matriz_existencias, lista_valores, "CABA")]
matriz_recaudaciones[1][2] = recaudacion_caba
recaudacion_chubut = [funciones.calcular_recaudacion_deposito(matriz_existencias, lista_valores, "Chubut")]
matriz_recaudaciones[1][3] = recaudacion_chubut
recaudacion_tucu = [funciones.calcular_recaudacion_deposito(matriz_existencias, lista_valores, "Tucumán")]
matriz_recaudaciones[1][4] = recaudacion_tucu
recaudacion_mend = [funciones.calcular_recaudacion_deposito(matriz_existencias, lista_valores, "Mendoza")]
matriz_recaudaciones[1][5] = recaudacion_mend

mayor_recaudacion = funciones.calcular_mayor_recaudacion(matriz_recaudaciones)
print(f"El depósito con la mayor recaudación fue: {mayor_recaudacion}")

# Punto 6 listo
print("\nPunto 6")
funciones.detectar_grandes_existencias(total_existencias_pba, "PBA")
funciones.detectar_grandes_existencias(total_existencias_caba, "CABA")
funciones.detectar_grandes_existencias(total_existencias_chubut, "Chubut")
funciones.detectar_grandes_existencias(total_existencias_tucu, "Tucumán")
funciones.detectar_grandes_existencias(total_existencias_mend, "Mendoza")








