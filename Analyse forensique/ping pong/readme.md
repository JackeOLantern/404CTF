**Objectif :** Dans ce challenge, il s'agit d'investiguer une communication et d'en relever les éléments intéressant la transmission.
Le suivi du protocole entre les interlocuteurs est tracé avec l'outil Wireshark.  Le dump au format 'pcap' fait découvrir que la longueur 
du champ de données des requetes en ping de paquets sur le réseau représente un caractère ASCII : à la base, on aurait plutôt envie d'extraire les données.
. D'ailleurs, le script scapy représente les nombreuses tentatives d'essais de combinaisons et de conversions à partir des données. Les caractères à l'intérieur
du Ping n'apportent rien de particulier. L'export s'effectue via un fichier binaire. Le flag obtenu est : 404CTF{Un_p1ng_p0ng_p4s_si_1nn0c3nt}.
