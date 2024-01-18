from os import system

BIN="./exos/p2/sc.o"

def main():
	# On execute la commande objdump pour obtenir le code assembleur
	system(f"objdump -d {BIN} > {BIN}.temporaire")

	# On ouvre le fichier contenant le code assembleur
	with open(f"{BIN}.temporaire", "r") as f:
		file = f.readlines()

	# On ne garde que les lignes qui commencent par un espace
	file = [line for line in file if line[0] == " "]

	# On supprime tout ce qui se trouve avant le premier ":"
	file = [line.split(":")[1] for line in file]

	# On supprime tout ce qui se trouve après le premier "\t"
	file = [line.split("\t")[0] for line in file]

	# On supprime les espaces de fin de ligne
	file = [line.strip() for line in file]

	# On met toutes les lignes sur une seule ligne
	file = " ".join(file)

	# On supprime les derniers caractères si c'est 00
	if file[-2:] == "00":
		file = file[:-3]

	# On remplace tout les espaces par des ", 0x"
	file = file.replace(" ", ", 0x")

	# On ajoute "0x" au début
	file = "0x" + file

	# On encadre par { }
	file = "{ " + file + " }"
	

	
	print(file)

	# On supprime le fichier contenant le code assembleur
	system(f"rm {BIN}.temporaire")

if __name__ == "__main__":
	main()
