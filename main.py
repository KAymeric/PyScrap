import sys

from scrapper import scrap


def main():
    args = sys.argv[1:]
    
    if not args:
        args.append(input("Please provide a URL to scrap : "))
    
    url = args[0]
    
    data = scrap(url)
    
    with open("data.txt", "w") as fichier:
        fichier.write(data)


if __name__ == "__main__":
    main()