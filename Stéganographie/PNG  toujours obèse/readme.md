**Objectif :** Dans ce challenge, on a l'image du challenge précédent qui a été obtenue par l'étape 2 et qui affiche un flag.
L'énoncé nous précise encore que le fichier est bien gros par rapport à ce qu'il contient.
On regarde à nouveau le contenu comme dans l'étape 2 mais cette fois-ci, rien n'apparaît avec l'éditeur de texte hexa du type HxD.
La structure du fichier PNG semble normale au premier abord avec son en-tête, les segments ("chunks") en data et l'IEND.
Il a été tenté des essais classiques (agrandir l'image, jouer sur les transparences, ...) mais cela n'a pas abouti à la solution.
: il y a encore une image masquée intégrées par l'image au premier plan d'affichage. 
Il est un prérequis à rappeler : image PNG est constituée d'une signature et d'une série de segments en séquence. 
https://www.commentcamarche.net/contents/1204-png-format-png#format-de-fichier-png. Dans ces segments, sont stockées 
les propriétés de l'image comme la couleur (R, V, B). Or, dans l'image globale, une première image PNG est déjà extraite 
et correspondant à l'image affichée courante.
Avec un outil qui visualise mieux la structure du PNG (par exemple: tweakPNG), on se rend compte de quelque chose d'anormal:
- il est composé de pleins de segments IDAT démarqués par une taille fixe (environ 8ko) sauf l'avant-dernier, qui est plus petit;
ce qui est classique (car il s'agit du reste des octets de l'image).
Sauf qu'il ne s'agit pas du dernier segment, comme supposé mais de l'avant-dernier en effet; le dernier à la suite étant beaucoup
plus gros que tous les autres segments (par exemple : 300 ko). Ce n'est pas interdit par la norme PNG mais reste très suspect.

Si on regarde le contenu du segment, en fait, on n'arrive pas à l'interpréter simplement et pour cause: comme les autres segments d'un PNG,
il est compressé comme c'est très souvent le cas.
Notre recherche s'oriente donc vers l'extraction des données du segment suspect : le protocole de compression des segments de PNG utilise 
un algorithme classique reconnu : zlib. Il existe peut-être d'autres stratégies de résolution, mais ici un script Python sert à l'extraction
du contenu.

Le programme de décodage *.PY à l'exécution décrit le procédé d'extraction des données imbriquées dans l'image d'origine avec 
la condition d'arrêt sur détection de fin (IEND). Les données qui contiennent normalement les couleurs de l'image, sont exportées 
au sein d'un fichier pour visualiser le contenu (last_data2.txt).
La plus grande partie du fichier est vide et sans intérêt 'il n'y a que du noir avec des code à zéro pendant des pages jusqu'à l'étiquette PNG)
Après 1250000 caractère inutiles (en position hexa :000E7120), il apparaît une nouveau fichier PNG complet avec sa zone de données (IDAT débutant
par IHDR) et qui va jusqu'à IEND: on conserve donc seulement la fin du fichier d'origine, commençant par l'en-tête PNG. On la sauve sous un nouveau
nom (ici, step3_fin.png) qui contient directement un troisième flag.

Voir la solution.
