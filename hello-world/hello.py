#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World - Le début d'une grande aventure en Python !
Fichier créé pour perpétuer la tradition du premier programme.
"""

def main():
    """Fonction principale du programme Hello World"""
    
    # La tradition du Hello World
    print("Hello, World!")
    print("Bonjour le monde !")
    print("¡Hola, Mundo!")
    print("🌍 Bienvenue dans l'univers Python ! 🐍")
    
    # Un peu d'information sur l'environnement
    print("\n" + "="*50)
    print("Informations sur votre environnement Python :")
    print("="*50)
    
    import sys
    import platform
    from datetime import datetime
    
    print(f"Version de Python : {sys.version}")
    print(f"Plateforme : {platform.system()} {platform.release()}")
    print(f"Date et heure : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Chemin de Python : {sys.executable}")
    
    # Un petit message motivant
    print("\n" + "="*50)
    print("🎉 Félicitations ! Votre premier programme Python est lancé !")
    print("💡 Conseil : La programmation est un art, prenez plaisir à créer !")
    print("🚀 Prêt(e) à explorer l'univers infini du code ?")
    print("="*50)


if __name__ == "__main__":
    # Point d'entrée du programme
    main()