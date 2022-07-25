**Objectif :** Dans ce challenge, l'objectif est de trouver un flag web en se logguant en tant qu'administrateur grâce à un cookie.
Il s'agit de bypasser la liste de rejet avec un padding adapté. On tente usuellement une injection de connexion avec privilège accru.
L'absence de traffic lors de la "vérification" du mot de passe implique que celle-ci se fait côté client (avec un hash à retrouver).   
....le serveur va vraisemblablement construire un tableau associatif à partir du cookie, à qui est ajouté =; (clef vide, valeur vide).


Le flag global est donc 404CTF{m3f13Z_V0Us_D3s_MdP_D4nS_L3s_c00k13s!}

Voir la solution.
