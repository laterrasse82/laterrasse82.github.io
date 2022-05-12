#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess as sp

def chargement():
    retour = sp.run(["git","pull"], capture_output=True, text=True).stdout.split("\n")
    
    for ligne in retour:
        print(ligne)
    
    print("###############################")

def sauvegarde():
    retour = sp.run(["git","add","*"], capture_output=True, text=True).stdout.split("\n")
    
    for ligne in retour:
        print(ligne)
    
    print("###############################")
    
    message = input("description des changements :")
    
    retour = sp.run(["git","commit","-m", message], capture_output=True, text=True).stdout.split("\n")
    
    for ligne in retour:
        print(ligne)
    
    print("###############################")
    
    retour = sp.run(["git","push"], capture_output=True, text=True).stdout.split("\n")
    
    for ligne in retour:
        print(ligne)
    
    print("###############################")
    
def main():
    retour = sp.run(["git","status"], capture_output=True, text=True).stdout.split("\n")
    
    for ligne in retour:
        print(ligne)
    
    print("###############################")
    
    message = input("""[]:exit\n[1]:récupérer depuis le serveur\n[2]:sauvegarder\n--> """)
    
    if message == "1":
        chargement()
    elif message == "2":
        sauvegarde()

if __name__ == "__main__":
    main()
