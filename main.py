def Login():
    print("Inicia Sesion")
    Usuario = input("Ingresa tu Usuario: ")
    Contraseña = input("Ingresa tu Contraseña: ")
    return Contraseña

def Verify_variety(Contraseña):
    Mayuscula = 0
    Verificacion_Mayuscula = False
    Minuscula = 0
    Numero = 0
    Simbolo = 0
    Verificacion_Numero = False
    Verificacion_Simbolo = False
    Verificacion_Variedad = False
    Verificacion_Largo = False
    for caracter in Contraseña:
        if caracter.isupper() == True:
            Mayuscula = Mayuscula + 1
            if Mayuscula >= 1:
                Verificacion_Mayuscula = True
        if caracter.islower() == True:
            Minuscula = Minuscula + 1
        if caracter.isdigit() == True:
            Numero = Numero + 1
            if Numero >= 3:
                Verificacion_Numero = True
        if not caracter.isalnum():
            Simbolo = Simbolo + 1
            if Simbolo >= 1:
                Verificacion_Simbolo = True

    Total_De_Letras = Mayuscula + Minuscula + Numero + Simbolo
    if Total_De_Letras >= 9:
        Verificacion_Largo = True

    if Verificacion_Numero and Verificacion_Mayuscula and Verificacion_Simbolo:
        Verificacion_Variedad = True

    return Verificacion_Variedad, Verificacion_Mayuscula, Verificacion_Largo

def Verificacion(Verificacion_Variedad, Verificacion_Mayuscula, Verificacion_Largo):
    if Verificacion_Variedad and Verificacion_Mayuscula and Verificacion_Largo:
        print("Verificacion Completa")
    else:
        print("Verifique su contraseña. Recuerde usar numeros, mayusculas y caracteres especiales ademas de tener una longitud de 12 caracteres")

def main():
    Contraseña_capturada = Login()
    Variedad, Mayuscula, Largo = Verify_variety(Contraseña_capturada)
    Verificacion(Variedad, Mayuscula, Largo)

main()