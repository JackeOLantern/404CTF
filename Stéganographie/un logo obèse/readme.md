**Objectif :** Dans ce challenge, il nous est fourni une image qui, quand on l'ouvre, n'affiche pas de flag comme on s'y attend.

La premi�re interrogation est de voir si on ne trouverait pas le flag dans le texte de l'image. On lance l'analyse du fichier sous Aperisolve (un mixte d'outils r�solvant les cas fr�quents de masquage par st�gano). L'op�ration via Binwalk donne un r�sultat probant.

Le d�but commence bien comme pr�vu par l'en-t�te d'un *.PNG: d'ailleurs, c'est une image PNG qui s'affiche dans un outil classique du style d'ImageViewer ou Paint.NET. A la fin, toutefois, on note les �l�ments caract�ristiques d'un fichier ZIP.
Pourquoi cela ne g�ne-t-il pas un fichier PNG de concat�ner un ZIP car une fois qu'il a lu le nombre d'octets indiqu�s dans son en-t�te, il s'arr�te de traiter les donn�es. On pense qu'il va falloir couper le fichier en Deux parties : le PNG qui correspond � l'image de base et la d�tacher de la fin des donn�es qui correspond � un fichier ZIP. En fait, Binwalk g�n�re lui-m�me la d�coupe du fichier en image redondante au format *.PNG lisible.

Le flag est alors inscrit en direct en haut de l'image � la forme d'une cassette audio : 404CTF{0b3z3_f13_h4z_zup3r_spy_s3cr37}

Voir la solution.
