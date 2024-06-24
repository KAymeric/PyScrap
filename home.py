def index(req):
    data = ""
    
    with open("data.txt", "r") as fichier:
        # Lire le contenu du fichier
        data = fichier.read()
    
    return data