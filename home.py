def index(req):
    data = ""
    
    with open("data.txt", "r+", encoding="utf-8") as fichier:
        # Lire le contenu du fichier
        data = fichier.read()
    
    return data

if __name__ == "__main__":
    print(index(None))