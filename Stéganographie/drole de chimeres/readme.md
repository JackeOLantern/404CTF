**Objectif :** Dans ce challenge il suffit de déterminer l'image réductible en retirant ses morceaux en doublons.

Les 8 premiers octets d'un fichier PNG sont identiques. Un PNG COMMENCE par :
89 50 4E 47 0D 0A 1A 0A 00 00 00 0D

et contient un IHDR puis se termine par un IEND

Or, celui ci cxntient 2 IHDR et 2 IEND donc 2 images et probablement mélangées ce qui empêche l'affichage de la deuxième: 
on va éliminer le bloc de data surnuméraire. Une d'entre elle s'appelle STEG donc on peut penser que c 'est celle ci qu"'on va garder
on supprime du second IHDR jusqu'au premier IEND incluant les >3 caractères de fin qui se retrouvent les deux cas soit 
49 45 4E 44 AE 42 60 82 .
La premère idée était de supprimer le bloc central donc en conservant le premier IHDR et le dernier IEND mais l'image ne s'affiche pas. Donc on essaie l'alternative : supprimer le début du premier IHDR jusqu'au début du second puis tout ce qui suit le dernier IEND ; ce tableau de bits étant censé se clore.
On élimine l'autre partie entre le premier bloc IHDR et le dernier IEND


On coupe l'image avec un outil gratuit HxD: on obtient un deuxième flag à l'édition affichée de l'image.

Voir la solution.
