"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""

def crearFacebook ():
    usuario = input("Ingrese el nombre de usuario: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
    pais = input("Ingrese el país en el que vive: ")
    correo = input("Ingrese su correo electrónico: ") 
    
    mensajeF = "\tFacebook\nUsuario: %s\nEdad: %d\nCiudad: %s\n"\
    "Pais: %s\nCorreo: %s"%(usuario, edad, ciudad, pais, correo) 
    return mensajeF

def crearTwitter ():
    usuario = input("Ingrese el nombre de usuario: ")
    nombres = input("Ingrese sus nombres: ")
    apellidos = input("Ingrese sus apellidos: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
    pais = input("Ingrese el país en el que vive: ")
    idioma = input("Ingrese el idioma: ")
    correo = input("Ingrese su correo electrónico: ") 
    print ("\tTwitter\nUsuario %s\nNombres: %s\nApellidos: %s\n"\
    "Edad: %d\nCiudad: %s\nPais: %s\nIdioma: %s\n"\
    "Correo: %s"%(usuario, nombres, apellidos, edad, ciudad, idioma, pais, correo))

def crearWhatsapp ():
    usuario = input("Ingrese el nombre de usuario: ")
    numero = int(input("Ingrese su número de celular: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
    pais = input("Ingrese el país en el que vive: ")
    mensajeF = "\tWhatsapp\nUsuario %s\nNumero de telefono: %d\nEdad: %d\nCiudad%s\n"\
    "Pais: %s"%(usuario, numero, edad, ciudad, pais) 
    return mensajeF

def crearTelegram ():
    usuario = input("Ingrese el nombre de usuario: ")
    numero = int(input("Ingrese su número de celular: "))
    ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
    pais = input("Ingrese el país en el que vive: ")
    interes = input ("Ingrese su área de interes: ")
    print("\tTelegram\nUsuario: %s\nNumero de telefono%d\nCiudad: %s\n"\
    "Pais: %s\nInteres personal: %s"%(usuario, numero, ciudad, pais, interes))

def crearsignal ():
    usuario = input("Ingrese el nombre de usuario: ")
    numero = int(input("Ingrese su número de celular: "))
    ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
    pais = input("Ingrese el país en el que vive: ")
    hobby = input("Ingrese su hobby favorito")
    mensajeF = "\tSignal\nUsuario: %s\nNumero de telefono: %d\nCiudad: %s\n"\
    "Pais: %s\nHobby favorito: %s"%(usuario, numero, ciudad, pais, hobby) 
    return mensajeF

def crearInstagram ():
    usuario = input("Ingrese el nombre de usuario: ")
    ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
    edad = int(input("Ingrese su edad: "))
    correo = input("Ingrese su correo electrónico: ")
    print("\tInstagram\nUsuario: %s\nCiudad: %s\nEdad: %d\n"\
    "Correo: %s"%(usuario, ciudad, edad, correo)) 

def crearFlickr ():
    usuario = input("Ingrese el nombre de usuario: ")
    correo = input("Ingrese su correo electrónico: ")
    mensajeF = "\tFlickr\nUsuario: %s\nCorreo: %s" %(usuario, correo)
    return mensajeF

def obtenerMensaje (nCuentas):
    mensaje_Final = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if (nCuentas >= 1) & (nCuentas <=5):
        cadena = mensaje_Final[0]
    elif (nCuentas >= 6 ) & (nCuentas <= 15):
        cadena = mensaje_Final[1]
    elif (nCuentas >= 16):
        cadena = mensaje_Final[2]
    return cadena
   
# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
if __name__ == "__main__": 
    bandera = True
    contador = 0 
    cadena = ""
    while(bandera):
        print("Ingresar una de las opciones")
        opcion = int(input("Ingresar 1 para crear una cuenta en Facebook\nIngresar 2 para crear una cuenta en Twitter\n"
        "Ingresar 3 para crear una cuenta en Whatsapp\nIngresar 4 para crear una cuenta en Telegram\n"
        "Ingresar 5 para crear una cuenta en Signal\nIngresar 6 para crear una cuenta en Instagram\n"
        "Ingresar 7 para crear una cuenta en Flickr:\n"))
        facebook = ""
        whatsapp = ""
        signal = ""
        flickr = ""
        if opcion == 1 :
            facebook = crearFacebook()
        else:
            if opcion == 2 :
                crearTwitter()
            else:
                if opcion == 3 :
                    whatsapp = crearWhatsapp()
                else:
                    if opcion == 4 :
                        crearTelegram()
                    else:
                        if opcion == 5 :
                            signal = crearsignal()
                        else:
                            if opcion == 6 :
                                crearInstagram()
                            else:
                                if opcion == 7 :
                                    flickr = crearFlickr()
        if ((opcion >= 1) & (opcion <= 7)):
            contador = contador + 1
        salida = input("Ingrese si para dejar de crear cuentas\n")
        if (salida == "si"):
            bandera = False
    print (facebook)
    print (whatsapp)
    print (signal)
    print (flickr)
    cadena = obtenerMensaje(contador)
    print (cadena)

