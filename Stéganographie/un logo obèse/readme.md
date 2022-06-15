**Objectif :** Dans ce challenge, il nous est fourni une image qui, quand on l'ouvre, n'affiche pas de flag comme on s'y attend.

La première interrogation est de voir si on ne trouverait pas le flag dans le texte de l'image. On lance l'analyse du fichier sous Aperisolve (un mixte d'outils résolvant les cas fréquents de masquage par stégano). L'opération via Binwalk donne un résultat probant.

Le début commence bien comme prévu par l'en-tête d'un *.PNG: d'ailleurs, c'est une image PNG qui s'affiche dans un outil classique du style d'ImageViewer ou Paint.NET. A la fin, toutefois, on note les éléments caractéristiques d'un fichier ZIP. La taille du logo est bien trop grande pour un petit logo.
Pourquoi cela ne gène-t-il pas un fichier PNG de concaténer un ZIP car une fois qu'il a lu le nombre d'octets indiqués dans son en-tête, il s'arrête de traiter les données. On pense qu'il va falloir couper le fichier en Deux parties : le PNG qui correspond à l'image de base et la détacher de la fin des données qui correspond à un fichier ZIP. En fait, Binwalk génère lui-même la découpe du fichier en une image redondante au format *.PNG lisible.

Le flag est alors inscrit en direct en haut de l'image à la forme d'une cassette audio : 404CTF{0b3z3_f13_h4z_zup3r_spy_s3cr37}

Voir la solution.
