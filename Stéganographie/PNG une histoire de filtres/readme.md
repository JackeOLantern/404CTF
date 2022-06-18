**Objectif :** Dans ce challenge, on a l'image du challenge précédent qui a été obtenue par l'étape 3 et qui affiche un flag. Il sert de base pour l'étape 4.
L'énoncé nous précise encore que le fichier est de taille trop élévée par rapport à une compression.
On regarde à nouveau le contenu comme dans l'étape 3 avec l'éditeur de texte hexa du type HxD et on se focalise sur le début de chaque ligne.
Hors indice, il est difficile de s'orienter vers une solution simple. Après avoir consulté la norme PNG, il existe un filtre qui est positionné sur le premier octet
de chaque ligne dans les segments en IDAT. En ouvrant avec HxD, on visualise le premier bit sur la première ligne qui vaut ici 0x1;
puis on avance de 800 *4 +1 octets(800 points par ligne et 4 octets par point plus 1 bit de filtre par ligne)et on trouve un deuxième octet de filtre.
Comme on ne va pas récupérer 600 octets de filtre ligne par ligne, on passe par un script automatisant l'extraction des octets à la suite.
Avec le nouveau programme png_deflate.PY, on extrait le fichier : step4_data.dat (l'extraction du fichier PNG source avec le même algo ZLIB de décompression que l'étape 3)
pour créer le fichier : step4_filter.dat ce dernier étant un sous-ensemble du premier ne contenant que les octets de filtrage.
L'ouverture du fichier dévoile un contenu avec les octets : 0, 1, 2, 3 ou 4 car les codes de filtres s'étalonnent de 0 à 4 dans la norme PNG). On constate aussi que les octets
sont bizarrement répartis : au début, il n'y a que des séquences de 0 à 3 pseudo-aléatoires sans motif répétitif apparent. A partir de la fin, on a de longues séquences de 4
qui semblent plus organisées. On s'intéresse à la première partie d'ordre variable dans laquelle les patterns n'apparaissent pas. On va décoder ces octets pour les transformer
en un entier en considérant qu'il est transcrit en base 4 (puisque ne contenant que des octets de 0 à 3); puis cet entier est affiché sous forme de chaine de caractères. 
La base 4 est affichée en code Hexa et pour chaque chiffre hexa, on prend le caractère ascii correspondant.
Le flag apparaît ASCII String: Secret code: 404CTF{7h3r3_15_n07h1n9_b4d_4b0u7_sc4nn3rz}

Voir la solution.
