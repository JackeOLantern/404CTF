**Objectif :** Dans cette étape 2 du challenge, on applique des filtres à l'outil wireshark pour analyser les flux de communication extraits du fichier pcap. 

1)ip.src == 192.168.122.55 and dns and dns contains "hallebarde".
2)On cherche les "never-gonna-give-you-up.hallebarde.404ctf.fr" qui sont au début de l'export de chaque fichier comme on le note dans le programme : exfiltration.py.
3)Dans l'appel dns suivant l'appel précédent, on a le nom des fichiers exportés en HEXA. On découvre en tout quatre fichiers dont les noms sont décodés soit par l'outil dcode.fr soit par un script PY : decodestep2.py.

Le code HEXA de ce qui obtenu par lecture de Wireshark donne : 

['666c61672e747874', '68616c6c6562617264652e706e67', '73757065722d7365637265742e706466', '657866696c74726174696f6e2e7079']
Une fois décodé en ASCII, 

['exfiltration.py', 'flag.txt', 'hallebarde.png', 'super-secret.pdf']

Les flag obtenu est donc 404CTF{exfiltration.py,flag.txt,hallebarde.png,super-secret.pdf}