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

print("Digite contraseña:")
password = input()
if validpass(password):
    print ("Contraseña válida")
