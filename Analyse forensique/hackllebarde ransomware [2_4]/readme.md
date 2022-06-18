**Objectif :** Dans ce challenge il suffit d'extraine une archive compressée.

Dans un premier temps on dezippe le fichier fourni et on a un fichier binaire énorme de l'état de la mémoire qui est d'extension .RAW (2 Go) brute.
On s'intéresse déjà aux chaînes de caractères qu'il contient: strings dumpmem.raw depuis le shell Linux. On obtient un fichier : strings.txt (160 Mo).
N'ayant pas d'autres pistes en vue, on investigue le contenu à la recherche d'éléments intéressants sur les critères : " SERVEUR, service, http, @ etc".
Au début du fichier (ligne 82242), on trouve cette ligne de paramètre : il s'agit juste d'une variable mais faisant référence à un serveur qui interpelle:4
SESSION_MANAGER=local/EVIL-SERV-81:@/tmp/.ICE-unix/1139,unix/EVIL-SERV-81:/tmp/.ICE-unix/1139
Il nous met sur une piste d'utilisation de ce mot-clé "EVIL-SERV-81". Ainsi à la ligne 263827, on trouve un compte : superadmin@EVIL-SERV-81 aussi suspect.
On avait découvert différents sites dont des centaines pouvant susciter l'intérêt d'un hacker. En effet, parmi ceux-là, il y a un manuel de débutant du hacking
qui nous semblait pas devoir être retenu en raison du fait qu'il ne s'agit pas d'une attaque intranet mais d'un cours disponible pour tous sur internet.
De facto, nous avions bien découvert au prime abord, trois champs pertinents sur quatre : l'adresse IP, le port et le nom du fichier malveillant (nom grossier).
Jusque là, sauf pour le quatrième champ de l'URL, il apparaît évident une fois obtenus, qu'ils font partie de la réponse recherchée. Il est plus étonnant que 
l'adresse de hack soit un site public de hacking éthique orienté vers les débutants qui est tout à fait légal et même digne d'intérêt pour un apprentissage.
Ainsi, en rejetant les adresses commerciales, par les routines fournies en solution de tri filtré, la source youtube doit être rétablie et supprimée du filtre.
Le flag formatté est donc le suivant : 404CTF{192.168.61.137:13598:JeNeSuisPasDuToutUnFichierMalveillant:https://www.youtube.com/watch?v=3Kq1MIfTWCE}
et non pas cet URL http://evil-serv-81/%7D à laquelle on avait préalablement pensé, car elle évoquait plus un serveur interne de cet environnement.
Voir la solution.
