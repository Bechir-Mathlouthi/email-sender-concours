"""
Script de lancement de l'interface graphique
"""

import sys
import os

def verifier_dependances():
    """Vérifie que toutes les dépendances sont installées"""
    try:
        import tkinter
        import pandas
        import fpdf
        import tqdm
        import openpyxl
        print("✅ Toutes les dépendances sont installées")
        return True
    except ImportError as e:
        print(f"❌ Dépendance manquante: {e}")
        print("📝 Installez les dépendances avec: pip install -r requirements.txt")
        return False

def main():
    """Fonction principale"""
    print("🎯 LANCEMENT DE L'INTERFACE GRAPHIQUE")
    print("=" * 50)
    
    # Vérifier les dépendances
    if not verifier_dependances():
        input("Appuyez sur Entrée pour quitter...")
        return
    
    # Vérifier les fichiers nécessaires
    fichiers_requis = ['config.py', 'pdf_generator.py', 'email_sender.py', 'interface_graphique.py']
    for fichier in fichiers_requis:
        if not os.path.exists(fichier):
            print(f"❌ Fichier manquant: {fichier}")
            input("Appuyez sur Entrée pour quitter...")
            return
    
    print("✅ Tous les fichiers sont présents")
    print("🚀 Lancement de l'interface graphique...")
    
    try:
        from interface_graphique import InterfaceEnvoiEmails
        app = InterfaceEnvoiEmails()
        app.run()
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")
        input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()
