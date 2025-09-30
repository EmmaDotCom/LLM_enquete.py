# --- Début du jeu ---
print("Bienvenue dans le jeu d'enquête avec IA !")
print("Un vol a eu lieu au manoir. Trois suspects sont présents :")
print("1. Majordome")
print("2. Jardinier")
print("3. Bibliothécaire")
print("Tape 'stop' à tout moment pour quitter.\n")

while True:
    choix = input("👉 Qui veux-tu interroger ? (1, 2 ou 3) : ")

    if choix.lower() == "stop":
        print("Enquête terminée. Merci d'avoir joué !")
        break
