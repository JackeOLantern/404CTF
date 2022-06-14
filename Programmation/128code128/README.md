**Objectif :** Dans ce challenge il y a une phrase qui est affich�e encod�e en base 64 bits.

Quand on la d�code, on obtient un fichier � en-t�te marqu� IHDR d'une image au format *.PNG.

On sauvegarde les bits obtenus par d�codage de base 64 : on obtient une image de codebarre.

On s'aper�oit qu'il s'agit de la [0/128] image et qu'il faut rapidement la d�coder pour avoir la suivante.


Seule l'automatisation de traitement permet de traiter les 129 images qui sont r�g�n�r�es distinctes � chaque appel afin d'obtenir le flag problablement apr�s la derni�re image exploit�e. 

Un code barre correspond � divers formats possibles
au vu du titre du challenge : 128 x 128, on comprend qu'il va y avoir 128 images et que le deuxi�me �l�ment "128" correspond � l'encodage du code barre.
On a les codes de traduction de toute la table ascii dans la page suivante.
https://fr.wikipedia.org/wiki/Code_128

Le script fourni fournit les �tapes suivantes :
1. connexion au Netcat
2. Extraction du texte en base64 de l'image
3. d�codage du texte en base 64
4. sauvegarde de l'image *.PNG

Pour la traiter automatiquement et pas visuellement, on convertit l'image *.PNG en RGB. 
On balaie les pixels de la gauche vers la droite avec la d�tection de lettres sur 11 unit�s (noires ou blanches successives).
Attention: il y a ici un pi�ge par rapport au format officiel qui nous a perturb� :
Il manque le caract�re de d�but et le stop qui devraient �tre l� mais n'y sont pas. On va les ignorer. On lit les bits 11 par 11 (1 pour noir et 0 pour blanc).
D�s qu'on obtient 11 codes (noirs ou blancs), on d�code la lettre.

Pour ce faire, on cr��e un dictionnaire � partir de la page wikipedia.
Par exemple :
d['10100011000']='A'
d['11001001110']='4'
d['10001000110']='C'

Ensuite, on concat�ne tous les caract�res obtenus et on les renvoie sur le serveur. Si la r�ponse est vue correcte, on obtient du serveur une nouvelle immage et on recommence l'op�ration. Apr�s la 128�me it�ration, on obtient le flag pour valider le challenge.

Voir la solution.
