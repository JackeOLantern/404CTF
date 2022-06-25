**Objectif :** Dans ce challenge, le jeu est impossible à gagner quand on voit le code source : choix_utilisateur = int(input("Choix ?\n> ")
En fait, on peut s'apercevoir que la faille est présente car la fonction d'entrée évalue la valeur saisie au lieu de la restituer telle quelle
(il s'agit d'une faille associée aux versions antérieures à python 2.x versus python 3.x à cause du passage de variable par valeurs calculées).
La petite faille qui a été trouvée : 
le input "évalue" ce qu'on saisit
Par exemple
saisis 1+1 tu vas voir
il fait comme si on avait saisi 2
autre essai (qui est défaillant)
mettre dans la valeur saisie
random.randint(1,3)
comme cela, le changement serait aléatoire.
Le flag est 404CTF{cH0iX_nUm3r0_4_v1c701r3}

Voir la solution.
