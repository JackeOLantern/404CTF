**Objectif :** Dans ce challenge, comme l'énoncé le suggère, on reçoit en se connectant au Netcat indiqué, des fragments de base 64; en tout cas, c'est ce qu'il semble au premier abord.

Une tentative de les décompresser fait apparaître plusieurs caractères non ascii à l'intérieur de la chaîne de caractères.
Ces caractères n'ayant pas le bon code perturbent le décodage des chaînes du fichier.

Or, ces caractères ne semblent pas "choisis" au hasard : ce sont des caractères provenant d'un autre alphabet (peut-être cyrillique, mais peu importe) très proches de leur représentation ascii.

On va reprendre par un script dédié les chaînes en pseudo-base 64 et remplacer les caractères non ascii par leurs équivalents ascii les plus proches.

Ensuite, on espère pouvoir décoder le résultat obtenu.

Au premier abord, en décodant les premiers caractères, il semble que l'en-tête du fichier commence par les caractères ID3 qui sont en principe typiques de fichiers audio MP3.

On assemble par concaténation les 250 fragments obtenus et on tente d'ouvrir le fichier ainsi produit avec un outil de type VLC (ou autre media player quelconque) : on entend une voix de synthèse féminine qui épelle le contenu du flag.

Voir la solution.
