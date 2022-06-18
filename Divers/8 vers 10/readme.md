**Objectif :** Dans ce challenge, ii y a un fichier texte qui contient des données décimales sous forme de données réelles.
L'énoncé nous évoque une communication sans nous en dire plus. Sans éléments additionnels, le flag est forcément dans ces données.
Une lecture rapide du fichier avec un éditeur de texte laisse entrevoir que les valeurs semblent osciller et paraissent bornées entre [-2,2]
ce qui nous fait penser à un signal analogique ayant une courbe  sinusoidale : la première étape est de la visualiser via le programme Python.
Si vous voulez le tester, poser la variable count = 300 (nombre de points) et décommenter les lignes Plot et Show en position 69 et 70.
On obtient la courbe résultante de la solution. En la voyant, elle fait clairement illustrer un signal analogique à deux valeurs : 2 et 1; 
que nous noterons 1 pour la valeur haute et 0 pour la valeur basse en binaire. Ensuite, le programme Python précédent va lire la courbe en balayant 
les crètes en les substituant en valeurs par 0 ou 1 (selon que le point est situé haut ou bas). Un fois le signal de la courbe décodé, on obtient 330 bits.
L'énoncé s'appelle "8 vers 10". Or, on a 330 bits qui est un multiple de 10 (et de 8). 8 bits nous fait penser à des caractères sur un octet (ascii).

100111010010011101101001110100101010001110101101001010100110110001101111001010111001010011101010001110011101101100101011100101001100111100101010110101001110110010010100111010110101100111001111001011011001110001100111011011001011011010110101001110001110101101010011100110100111010000111000111001110001001110110010010100111100011101


De plus, quand on coupe la chaîne de caractères par paquets de 10, on obtient :
1001110100 1001110110 1001110100 1010100011 1010110100 1010100110 1100011011 1100101011 1001010011 1010100011 1001110110 1100101011 1001010011 0011110010 1010110101 0011101100 1001010011 1010110101 1001110011 1100101101 1001110001 1001110110 1100101101 
1010110101 0011100011 1010110101 0011100110 1001110100 0011100011 1001110001 0011101100 1001010011 1100011101
﻿
Par exemple, le groupement 1 est égal au groupe 3 (comme dans "404"). Il semblerait qu'on soit en présence directe du flag.
A ce niveau-là, je me suis pas mal embourbée. Il faut trouver une règle pour convertir ces 10 bits en 8 bits (transformation en décodage réciproque).
Pas mal de recherche a eu lieu sur internet pour trouver les encodages classiques de signaux analogiques. Il y a manifestement une modulation d'amplitude.
Les articles nous en renvoyé vers des typologies d'encodages (type Manchester etc.) mais aucun des types n'a fonctionné car ce n'était pas le bon encodage.
Enfin, il s'est avéré, que l'information était en fait dans le titre du challenge, car l'encodage est du 8b/10b :
https://en.wikipedia.org/wiki/8b/10b_encoding. Coup de chance : l'implémentation existe en Python avec une bibliothèque qui se nomme: EncDec8B10B.

La stratégie est donc la suivante : on prend les paquets découpés ci-dessus 10 bits en binaire qui deviennent 2 octets en Hexa et on appelle le décodage 
par la librairie fournie caractère par caractère.
Le flag est présent à la concaténation de la réponse lors de l'exécution du script : 404CTF{d3C0d3r_l3_8b10b_c_f4c1l3}

Voir la solution.
