def validname(unsername):
    if (len(username)<6):
        print("El nombre de usuario debe contener al menos 6 caracteres")
    elif  (len(username)>12):
        print("El nombre de usuario no puede contener más de 12 caracteres")
    elif not(username.isalnum()):
        print("El nombre de usuario puede contener solo letras y números")
    else:
        return True

print("¿Digite nombre de usuario?")
username = input()
if validname(username):
    print ("Nombre válido")
