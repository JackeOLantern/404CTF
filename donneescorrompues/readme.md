**Objectif :** Dans ce challenge, comme l'�nonc� le sugg�re, on re�oit en se connectant au Netcat indiqu�, des fragments de base 64; en tout cas, c'est ce qu'il semble au premier abord.

Une tentative de les d�compresser fait appara�tre plusieurs caract�res non ascii � l'int�rieur de la cha�ne de caract�res.
Ces caract�res n'ayant pas le bon code perturbent le d�codage des cha�nes du fichier.

Or, ces caract�res ne semblent pas "choisis" au hasard : ce sont des caract�res provenant d'un autre alphabet (peut-�tre cyrillique, mais peu importe) tr�s proches de leur repr�sentation ascii.

On va reprendre par un script d�di� les cha�nes en pseudo-base 64 et remplacer les caract�res non ascii par leurs �quivalents ascii les plus proches.

Ensuite, on esp�re pouvoir d�coder le r�sultat obtenu

Au premier abord, en d�codant les premiers caract�res, il semble que l'en-t�te du fichier commence par les caract�res ID3 qui sont en principe typiques de fichiers audio MP3.

On assemble par concat�nation les 250 fragments obtenus et on tente d'ouvrir le fichier ainsi produit avec un outil de type VLC (ou autre media player quelconque) : on entend une voix de synth�se f�minine qui �pelle le contenu du flag.

Voir la solution.
