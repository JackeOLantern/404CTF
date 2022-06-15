**Objectif :** Dans ce challenge il y a une phrase qui est affichée encodée en base 64 bits.

Quand on la décode, on obtient un fichier à en-tête marqué IHDR d'une image au format *.PNG.

On sauvegarde les bits obtenus par décodage de base 64 : on obtient une image de codebarre.

On s'aperçoit qu'il s'agit de la [0/128] image et qu'il faut rapidement la décoder pour avoir la suivante.


Seule l'automatisation de traitement permet de traiter les 129 images qui sont régénérées distinctes à chaque appel afin d'obtenir le flag problablement après la dernière image exploitée. 

Un code barre correspond à divers formats possibles
au vu du titre du challenge : 128 x 128, on comprend qu'il va y avoir 128 images et que le deuxième élément "128" correspond à l'encodage du code barre.
On a les codes de traduction de toute la table ascii dans la page suivante.
https://fr.wikipedia.org/wiki/Code_128

Le script fourni fournit les étapes suivantes :
1. connexion au Netcat
2. Extraction du texte en base64 de l'image
3. décodage du texte en base 64
4. sauvegarde de l'image *.PNG

Pour la traiter automatiquement et pas visuellement, on convertit l'image *.PNG en RGB. 
On balaie les pixels de la gauche vers la droite avec la détection de lettres sur 11 unités (noires ou blanches successives).
Attention: il y a ici un piège par rapport au format officiel qui nous a perturbé :
Il manque le caractère de début et le stop qui devraient être là mais n'y sont pas. On va les ignorer. On lit les bits 11 par 11 (1 pour noir et 0 pour blanc).
Dès qu'on obtient 11 codes (noirs ou blancs), on décode la lettre.

Pour ce faire, on créée un dictionnaire à partir de la page wikipedia.

Par exemple :
d['10100011000']='A'
d['11001001110']='4'
d['10001000110']='C'

Ensuite, on concatène tous les caractères obtenus et on les renvoie sur le serveur. Si la réponse est vue correcte, on obtient du serveur une nouvelle image et on recommence l'opération. Après la 128ème itération, on obtient le flag pour valider le challenge.

Voir la solution.
