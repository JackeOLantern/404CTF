**Objectif :** Dans ce challenge, il est recherché la source qui a envoyé le plus donné avec la statistique de Wireshark.
On extrait les données envoyées par l'émetteur dans un fichier : on filtre que la source soit l'adresse IP de l'émetteur.
Le programme scapy permet de scripter l'extraction des données issues de Wireshark en extrayant les packets sur 2 octets 
(en effet, hormis deux otets significatifs, de l'en-têtes, les autres informations se répètent mais sont non pertinentes.)
Le flag est présent dans le fichier PDF obtenu par construction à partir de ces octets : 404CTF{L3s_fL4gS_TCP_Pr1S_3n_fL4G}
Voir la solution.
