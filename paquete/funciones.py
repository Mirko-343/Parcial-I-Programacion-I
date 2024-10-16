# Mirko Becker

def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any) -> list:
    ''' Inicializa una matriz en base a los valores recibidos por parámetros.
        El primer parámetro es la cantidad de filas. El segundo la cantidad de columans y el tercero
        el valor incial con el que se van a completar las casillas.
        Devuelve la matriz '''
        
    matriz = []
    
    for i in range(cantidad_filas):
        fila = cantidad_columnas * [valor_inicial]
        matriz += [fila]
        
    return matriz

def completar_matriz_existencias(matriz_existencias : list) -> list:
    ''' Función auxiliar utilizada para completar los valores fijos de la matriz de existencias.
        Recibe como paráemtero la matriz de existencias vacía '''
    
    if type(matriz_existencias) != list:
        print("El parámetro recibido no es del tipo correcto")
        return None

    matriz_existencias[0][1] = "PBA"
    matriz_existencias[0][2] = "CABA"
    matriz_existencias[0][3] = "Chubut"
    matriz_existencias[0][4] = "Tucumán"
    matriz_existencias[0][5] = "Mendoza"
    
    matriz_existencias[1][0] = "Autos"
    matriz_existencias[2][0] = "Muñecas"
    matriz_existencias[3][0] = "Trenes"
    matriz_existencias[4][0] = "Peluches"
    matriz_existencias[5][0] = "Spinners"
    matriz_existencias[6][0] = "Cartas"
    
    return matriz_existencias

def cargar_existencias(matriz_existencias : list, deposito : str, lista_existencias : list) -> list:
    ''' Permite cargar las existencias de cada depósito en la matriz de existencias.
        Recibe como primer parámetro la matriz de existencias base con los valores fijos ya cargados.
        Como segundo parámetro recibe el nombre del depósito para el cual se quieren cargar las existencias
        Como tercer parámetro recibe la lista con las existencias del depósito correspondiente. Los valores
        tienen que estar organizados de la siguiente manera
        1.autos 2.muñecas 3.trenes 4.peluches 5.spinners 6.cartas
        Devuelve la matriz de existencias con los valores cargados '''
        
    if type(matriz_existencias) != list or type(lista_existencias) != list or type(deposito) != str:
        print("Uno de los parámetros recibidos no es del tipo correcto")
        return None
        


    for i in range(len(matriz_existencias[0])):
        if matriz_existencias[0][i] == deposito:
            matriz_existencias[1][i] = lista_existencias[0]
            matriz_existencias[2][i] = lista_existencias[1]
            matriz_existencias[3][i] = lista_existencias[2]
            matriz_existencias[4][i] = lista_existencias[3]
            matriz_existencias[5][i] = lista_existencias[4]
            matriz_existencias[6][i] = lista_existencias[5]

    return matriz_existencias
            
def mostrar_matriz(matriz : list) -> None:
    ''' Función que se encarga de recorrer y mostrar la lista que recibe por parámetro '''
    
    if type(matriz) != list:
        print("El parámetro recibido no es del tipo correcto")
        return None

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"Fila {i} Columna {j}: {matriz[i][j]}")
                        
def calcular_total_existencias(matriz_existencias : list, deposito : str) -> int:
    ''' Calcula el total de existencias por depósito sumando el total de todos los tipos de juguete
        Como primer parámetro recibe la matriz de existencias con los valores fijos y varibales ya cargados
        Como segundo parametro recibe el nombre del depósito para el cual se quiere hacer el cálculo
        Devuelve un entero con el total de existencias '''
      
    if type(matriz_existencias) != list:
        print("El parámetro recibido no es del tipo correcto")
        return None
        
    total_existencias = 0

    for i in range(len(matriz_existencias[0])):
        if matriz_existencias[0][i] == deposito:
            n = len(matriz_existencias)
            for j in range(n):
                if j == 0:
                    continue
                else:
                    total_existencias += matriz_existencias[j][i]
                
    return total_existencias

def detectar_escacez(matriz_existencias : list, cantidad_minima : int) -> None:
    ''' Calcula los juguetes que necesitan reposición en cada depósito.
        Como primer parámetro recibe la matriz de existencias con los valores fijos y variables ya cargados
        Como segundo parámetro recibe la cantidad mínima de juguetes que puede haber de cada tipo '''
     
    if type(matriz_existencias) != list or type(cantidad_minima) != int:
        print("Uno de los parámetros recibidos no es del tipo correcto")
        return None
        
    for i in range(len(matriz_existencias)):
        for j in range(len(matriz_existencias[i])):
            if i != 0 and j != 0:
                if matriz_existencias[i][j] < cantidad_minima:
                    # Si acomodo el print para que entre en la pantalla me da un error que no se a qué se debe así que prefiero dejarlo
                    # así por ahora. Se que no cumple con las reglas de estilo.
                    print(f"Es necesario reponer {matriz_existencias[i][0]} en el depósito de {matriz_existencias[0][j]}. Hay solamente {matriz_existencias[i][j]}")
                    
                else:
                    continue
                
def calcular_mayor_existencia(matriz_existencias : list) -> None:
    ''' Calcula en qué depósito se encuentra la mayor existencia de cada juguete.
        Como primer parámetro recibe la matriz de existencias con los valores fijos y variables ya cargados
        Devuelve un print con la infromación '''
      
    if type(matriz_existencias) != list:
        print("El parámetro recibido no es del tipo correcto")
        return None
        
    for i in range(len(matriz_existencias)):
        bandera = False
        mayor_existencia = 0
        deposito = "a"
        for j in range(len(matriz_existencias[0])):
            if i != 0 and j != 0:
                if bandera == False:
                    bandera = True
                    mayor_existencia = matriz_existencias[i][j]
                    deposito = matriz_existencias[0][j]
                elif matriz_existencias[i][j] > mayor_existencia:
                    mayor_existencia = matriz_existencias[i][j]
                    deposito = matriz_existencias[0][j]
        if i != 0 and j != 0:
            print(f"La mayor existencia de {matriz_existencias[i][0]} se encuentra en el depósito de {deposito}. {mayor_existencia} unidades")
                       
def calcular_recaudacion_deposito(matriz_existencias : list, lista_valores : list, deposito : str) -> int:
    ''' Calcula la recaudación total de un depósito.
        Como primer parámetro recibe la matriz de existencias con los valores fijos y variables ya cargados.
        Como segundo parámetro recibe una lista con el valor de cada tipo de juguete ordenado de la siguiente manera:
        1.auto 2.muñeca 3.trenes 4.peluches 5.spinners 6.cartas 
        Como tercer parámetro recibe el nombre del depósito para el que se quiere hacer el cálculo 
        Devuelve un entero con la recaudación  total '''
     
    if type(matriz_existencias) != list or type(lista_valores) != list or type(deposito) != str:
        print("Uno de los parámetros recibidos no es del tipo correcto")  
        return None

    recaudacion_total = 0
    
    for i in range(len(matriz_existencias[0])):
        if matriz_existencias[0][i] == deposito:
            n = len(matriz_existencias)
            contador = 0
            for j in range(n):
                
                if j == 0:
                    continue
                else:
                    recaudacion_total += (matriz_existencias[j][i] * lista_valores[contador])
                    contador += 1
                
    return recaudacion_total

def completar_matriz_recaudaciones(matriz_recaudaciones : list) -> list:
    ''' Completa la matriz de recaudaciones con los valores fijos
        Devuelve la matriz con los datos cargados '''
     
    if type(matriz_recaudaciones) != list:
        print("Uno de los parámetros recibidos no es del tipo correcto")
        return None
        
    matriz_recaudaciones[0][1] = "PBA"
    matriz_recaudaciones[0][2] = "CABA"
    matriz_recaudaciones[0][3] = "Chubut"
    matriz_recaudaciones[0][4] = "Tucumán"
    matriz_recaudaciones[0][5] = "Mendoza"
    
    return matriz_recaudaciones

def calcular_mayor_recaudacion(matriz_recaudaciones : list) -> str:
    ''' Calcula el depósito con mayor recaudación.
        Recibe como primer parámetro la matriz de recaudaciones con los campos fijos y variables ya cargados
        Devuelve un String con el nombre del depósito que tuvo la mayor recaudación '''
        
    if type(matriz_recaudaciones) != list:
        print("Uno de los parámetros recibidos no es del tipo correcto")
        return None

    bandera = False
    for i in range(len(matriz_recaudaciones[0])):
        if i != 0:
            if bandera == False:
                mayor_recaudacion = matriz_recaudaciones[1][i]
                deposito = matriz_recaudaciones[0][i]
                bandera = True
            elif matriz_recaudaciones[1][i] > mayor_recaudacion:
                mayor_recaudacion = matriz_recaudaciones[1][i]
                deposito = matriz_recaudaciones[0][i]
                
    return deposito
                
def detectar_grandes_existencias(existencias_deposito : int, deposito : str) -> None:
    ''' Calcula los depósitos que acumularon más de 50000 unidades sumando todos los tipos
        Como primer parámetro recibe el total de las existencias del depósito.
        Como segundo parámetro recibe el nombre del depósito por el que se quiere filtrar.
        Devuelve un print informando solamente aquellos depósitos que superaron las 50000 unidades'''
    
    if type(existencias_deposito) != int or type(deposito) != str:
        print("Uno de los parámetros recibidos no es del tipo correcto")
        return None
        
    if existencias_deposito > 50000:
        print(f"El depósito de {deposito} superó las 50.000 unidades almacenadas entre todos los juguetes")
        


    
