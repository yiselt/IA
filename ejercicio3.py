def validname(unsername):
    if (len(username)<6):
        print("El nombre de usuario debe contener al menos 6 caracteres")
    elif  (len(username)>12):
        print("El nombre de usuario no puede contener más de 12 caracteres")
    elif not(username.isalnum()):
        print("El nombre de usuario puede contener solo letras y números")
    else:
        return True

def validpass(password):
    if (len(password)<8):
        print("La contraseña debe contener un mínimo de 8 caracteres")
    elif  (password.find(' ')> -1):
        print("La contraseña no debe contener espacios")
    else:
        indice=0
        mayusculas=0
        minusculas=0
        digitos=0
        alnum=0
        while indice < len(password):
          letra = password[indice]
          if letra.isupper() == True:
            mayusculas +=1
          elif letra.islower() == True:  
            minusculas +=1
          elif letra.isdigit() == True:
            digitos += 1
          elif not(letra.isalnum()) == True:
            alnum += 1
          indice += 1
        if mayusculas*minusculas*digitos*alnum == 0:
            print("La contraseña debe contener contener mayúsculas, minúsculas, números y caracteres especiales")
        else:
            return True

userOk=False
passOk=False
while not(userOk):
    print("Digite Usuario")
    username = input()
    if validname(username):
        print ("Nombre válido")
        userOk=True

while not(passOk):
    print("Digite contraseña:")
    password = input()
    if validpass(password):
        print ("Contraseña válida")
        passOk=True

print("Datos validos: ",username,password)
