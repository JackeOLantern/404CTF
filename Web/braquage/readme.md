**Objectif :** Dans ce challenge, l'objectif est de trouver différents flags successifs à travers des formulaires qui laissent à penser à des injections SQL.
Un premier essai avec une injection SQL du type OR suggéré par le nom de la page "les vendeurs d'OR" conduit à déceler deux flags dans une même table.
Un deuxième essai avec l'union select permet d'aller sélectionner une autre table et ses contenus et donc accéder à d'autres données. Il se trouve que des flags y sont cachés.


Voir la solution.
