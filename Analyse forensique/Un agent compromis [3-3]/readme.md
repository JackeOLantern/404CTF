**Objectif :** Dans cette étape 3 du challenge, on doit cette fois-ci extraire les données contenues dans les fichiers par Wireshark. 
1) Le début des données correspond à un appel dns : cet appel DNS 626567696E.hallebarde.404ctf.fr
   La fin des données correspond à cet appel dns : 656E64.hallebarde.404ctf.fr
2) Entre les deux appels, on a les code HEXA des data. Le premier fichier est flag.txt qui paraît le plus prometteur. Malheureusement, quand on décode ses données en HEXA ,on obtient : 
 
 ['404CTF{pas le fl', 'ag, dommage :p}\n']
 
 3) On passe au fichier suivant qui est le fichier Hallebarde.png mais qui est juste un logo sans flag de la Hallebarde.
 
 4) On arrive au 3ième fichier qui est : exfiltration.py que l'on avait déjà et qui contient bien un flag mais celui de l'étape 1.
 
 5) On extrait le dernier fichier qui est un fichier pdf appelé : super-secret.pdf qui semble corrompu car il est blanc en contenu quand on l'ouvre.
 Il apparaît donc qu'il faille travailler sur le fichier super-secret.pdf pour déduire le flag restant pour l'instant masqué. On essaie de l'ouvrir avec un éditeur de texte de type : notepad.
 En fait, en ouvrant le fichier PDF, on ne trouve pas de flag directement mais il existe des streams de données à l'intérieur du PDF. En PDF, les streams sont des données comprimées avec 
 une librairie appelée zlib, dont l'implémentation existe en python. Ci-joint le fichier : extractPDStreams.py qui se trouve dans le lot zippé en solution.
 
 Quand le décompresse, on obtient trois sorties appelées : out1.bin, out2.bin et out3.bin.
 En fait, quand on ouvre ces fichiers binaires par un éditeur de texte notepad, on voit que out1 et out3 contiennent des zones textuelles.
 le fichier : out3.bin est particulièrement intéressant: il contient un encodage de lettres de type flag : "4; 0; C; T; F; {...etc". Mais qu'en faire?
 On a réouvert le fichier out1.bin et là, on voit entre des chevrons <0102010304> etc , les codes de out3.bin.

Les data du flag à décoder sont : <0102010304><05><06><07><08><09><0A0B0C0D0E0F><10><1101><10><0E02120A1314><0F><0F><15><1614><111715><18>
On enlève les <> et on prend les codes de caractères deux par deux : 

La table de décodage est la suivante : 
<01> <0034> 4
<02> <0030> 0
<03> <0043> C
<04> <0054> T
<05> <0046> F
<06> <007B> {
<07> <0044> D
<08> <004E> N
<09> <0053> S
<0A> <005F> _
<0B> <0033> 3
<0C> <0078> x
<0D> <0066> f
<0E> <0031> 1
<0F> <006C> l
<10> <0074> t
<11> <0072> r
<12> <006E> n
<13> <0068> h
<14> <0061> a
<15> <0065> e
<16> <0062> b
<17> <0064> d
<18> <007D> }

4 0 4 C T F { D N S  3 x f 1 l t r 4 t 1 0 n  h a l l e b a r d e }


404CTF{DNS_3xf1ltr4t10n_hallebarde}
