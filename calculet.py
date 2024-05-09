nombr1=float(input("entre le nombre un :"))
nombr2=float(input("entre le nombre deux : "))
sympole=input("voulez vous faire quel type d'operation x : + - entree une signe de votre choix ")
if sympole=="x":
    reponse=nombr1*nombr2
    print("la reponse est :",reponse)
elif sympole==":":
    if nombr2 !=0:
        reponse=nombr1/nombr2
        print("la reponse est :",reponse)
    else:
        print("imposible de calculer car on ne peut pas diviser un nombre par zèro ")     
elif sympole=="-":
    reponse=nombr1-nombr2
    print("la reponse est :",reponse)
elif sympole=="+":
    reponse=nombr1+nombr2
    print("la reponse est :",reponse)
