#Esta línea define la función dibujar_ahorcado y toma un parámetro llamado intentos_restantes, que se utilizará para determinar qué fase del ahorcado se debe mostrar.
def dibujar_ahorcado(intentos_restantes):

  #Aquí se crea una lista llamada ahorcado, que contiene representaciones en formato de cadena de texto de cada fase del ahorcado. Cada elemento de la lista es una cadena de varias líneas que representa el dibujo correspondiente al ahorcado en un estado específico.
    ahorcado = [
        '''
         --------
         |      |
         |
         |
         |
         |
        ---
        '''
        ,
        '''
         --------
         |      |
         |      O
         |
         |
         |
        ---
        '''
        ,
        '''
         --------
         |      |
         |      O
         |      |
         |
         |
        ---
        '''
        ,
        '''
         --------
         |      |
         |      O
         |     /|
         |
         |
        ---
        '''
        ,
        '''
         --------
         |      |
         |      O
         |     /|\\
         |
         |
        ---
        '''
        ,
        '''
         --------
         |      |
         |      O
         |     /|\\
         |     /
         |
        ---
        '''
        ,
        '''
         --------
         |      |
         |      O
         |     /|\\
         |     / \\
         |
        ---
        '''
    ]
#esta función se encarga de mostrar un diagrama del ahorcado en la consola, que evoluciona a medida que el jugador comete errores durante el juego.
    print(ahorcado[max(0, len(ahorcado) - intentos_restantes - 1)])