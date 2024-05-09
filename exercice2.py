fruit="jaune"
match fruit:
    case "vert":
        print("non mur")
    case "rouge" :
        print("fruit mur")
    case "jaune" :
        print("fruit pourie")
    case _:
        print("je ne sais pas")
