""" conjunto = {20, 17, 12, 8, 4, 3, 12, 1, 18, 3, 18, 2, 12, 11, 1}
print(conjunto) """


usuarios = {
    "email":[],
    "contrasena":[]
}



#Registro
for i in range(2):
    correo = input("Ingrese su correo: ")
    contra = input("Ingrese su contraseña: ")

    usuarios["email"].append(correo)
    usuarios["contrasena"].append(contra)


#Acceso
correo = input("Ingrese su correo_Acceso: ")
contra = input("Ingrese su contraseña_Acceso: ")
contador = 0
validacion = False

for i in usuarios["email"]:
    if i == correo:
        validacion = True
        break
    contador+=1

if usuarios["contrasena"][contador] == contra:
    validacion = True
else:
    validacion = False

if validacion == True:
    print("Login correcto!!!!")
else:
    print("Login Incorrecto!!!!")




#print(usuarios)