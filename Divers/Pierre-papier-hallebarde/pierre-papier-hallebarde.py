#!/usr/bin/python2.7 -u
# -*- coding: utf-8 -*-

choix = {1 : "pierre", 2 : "papier", 3 : "Hallebarde"}

def bonjour():
	print("Bienvenue sur pierre-papier-Hallebarde !")
	print("La pierre bat la Hallebarde, le papier bat la pierre et la Hallebarde bat le papier")
	print("Pour jouer entrez un chiffre entre 1 et 3 : ")
	print("1 : pierre")
	print("2 : papier")
	print("3 : Hallebarde")

def jouer():
	choix_utilisateur = int(input("Choix ?\n> "))

	if choix_utilisateur == 1:
		choix_ordi = 2
	elif choix_utilisateur == 2:
		choix_ordi = 3
	elif choix_utilisateur == 3:
		choix_ordi = 1
	else:
		print("Choix invalide. Vous avez perdu")
		exit(1)

	print("Vous avez choisi : " + choix[choix_utilisateur] + ". L'ordinateur a choisi : " + choix[choix_ordi] +".")
	if decision(choix_utilisateur, choix_ordi) == 1:
		print("Vous avez gagné !!! Incroyable !")
		f = open("flag.txt", "r")
		print(f.readline())
		f.close()
	else :
		print("Vous avez perdu...")

def decision(joueur1, joueur2):

	if joueur1 == joueur2:
		return 2
	if joueur1 == 1 and joueur2 == 2:
		return 2
	if joueur1 == 1 and joueur2 == 3:
		return 1
	if joueur1 == 2 and joueur2 == 1:
		return 1
	if joueur1 == 2 and joueur2 == 3:
		return 2
	if joueur1 == 3 and joueur2 == 1:
		return 2
	if joueur1 == 3 and joueur2 == 2:
		return 1
	return 2

def main():
	bonjour()
	while True:
		jouer()


if __name__ == "__main__":
	main()
