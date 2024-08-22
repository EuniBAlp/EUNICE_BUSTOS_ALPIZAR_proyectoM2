#LONGITUD DE UNA PALABRA O CONTRASEÑA#
palabra1= input ("Introduce la primer palabra")
palabra2= input ("Introduce la segunda palabra")
palabra3= input ("Introduce la tercer palabra")
palabra4= input ("Introduce la cuarta palabra")
#CUANDO LA PALABRA TIENE MENOS DE 4 CARACTERES SE AGREGA X#
if len (palabra1) < 4: 
    palabra1= "X" + palabra1
if len (palabra2) < 4:
    palabra2= "X" + palabra2
if len (palabra3) < 4:
    palabra3= "X" + palabra3
if len (palabra4) < 4:
    palabra4= "X"+ palabra4 
#RE ARROJA LA CONTRASEÑA#
contraseña= palabra1[0]+palabra2[0]+palabra3[0]+palabra4[0]+palabra1[1]+palabra2[1]+palabra3[1]+palabra4[1]
print("La contraseña es:", contraseña)
#SOLICITA CONTRASEÑA AL USUARIO#
contraseña_usuario= input("Introduce la contraseña, por favor:")
#INFORMA SI FALTAN CARACTERES EN LA CONTRASEÑA#
if len (contraseña_usuario) < len (contraseña):
    print ("Faltan", len (contraseña)-len (contraseña_usuario),"caracteres")
contraseña_usuario= input ("Introduce de nuevo la contraseña, por favor:")
#INFORMA SI SOBRAN CARACTERES EN LA CONTRASEÑA#
if len (contraseña_usuario) > len (contraseña):
    print ("Sobran", len (contraseña) - len (contraseña_usuario),"caracteres")
contraseña_usuario= input ("Introduce de nuevo la contraseña, por favor:")
#INFORMA SI LA CONTRASEÑA ES CORRECTA O INCORRECTA#
if contraseña_usuario==contraseña:
    print ("CONTRASEÑA CORRECTA")
else: 
    print("CONTRASEÑA INCORRECTA,")
