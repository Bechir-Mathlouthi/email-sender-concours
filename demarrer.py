"""
Script de démarrage simple pour le système d'envoi d'emails
"""

import os
import sys

def afficher_menu():
    """Affiche le menu principal"""
    print("🎯 SYSTÈME D'ENVOI D'EMAILS PERSONNALISÉS")
    print("=" * 50)
    print("1. 🔧 Configurer l'email (première fois)")
    print("2. 🧪 Tester le système")
    print("3. 📊 Créer un fichier Excel d'exemple")
    print("4. 🖥️ Interface Graphique (NOUVEAU!)")
    print("5. 🚀 Lancer l'envoi d'emails (ligne de commande)")
    print("6. 📖 Afficher le guide")
    print("7. ❌ Quitter")
    print("=" * 50)

def verifier_configuration():
    """Vérifie si la configuration est faite"""
    try:
        from config import EMAIL_CONFIG
        if EMAIL_CONFIG['expediteur'] == 'votre.email@example.com':
            return False
        return True
    except:
        return False

def main():
    """Fonction principale"""
    while True:
        afficher_menu()
        
        choix = input("\n❓ Choisissez une option (1-7) : ").strip()

        if choix == '1':
            print("\n🔧 Configuration de l'email...")
            os.system('python configurer_email.py')

        elif choix == '2':
            if not verifier_configuration():
                print("\n❌ Vous devez d'abord configurer l'email (option 1)")
                continue
            print("\n🧪 Test du système...")
            os.system('python test_system.py')

        elif choix == '3':
            print("\n📊 Création d'un fichier Excel d'exemple...")
            os.system('python creer_exemple_excel.py')

        elif choix == '4':
            print("\n🖥️ Lancement de l'interface graphique...")
            os.system('python lancer_interface.py')

        elif choix == '5':
            if not verifier_configuration():
                print("\n❌ Vous devez d'abord configurer l'email (option 1)")
                continue

            if not os.path.exists('candidats_selectionnes.xlsx'):
                print("\n❌ Fichier candidats_selectionnes.xlsx non trouvé")
                print("📝 Créez d'abord votre fichier Excel avec les données des candidats")
                continue

            print("\n🚀 Lancement de l'envoi d'emails...")
            os.system('python main.py')

        elif choix == '6':
            print("\n📖 Ouverture du guide de configuration...")
            if os.path.exists('GUIDE_INTERFACE_GRAPHIQUE.md'):
                # Essayer d'ouvrir avec l'éditeur par défaut
                try:
                    os.startfile('GUIDE_INTERFACE_GRAPHIQUE.md')
                except:
                    print("📄 Consultez le fichier GUIDE_INTERFACE_GRAPHIQUE.md")
            else:
                print("❌ Guide non trouvé")

        elif choix == '7':
            print("\n👋 Au revoir !")
            break

        else:
            print("\n❌ Option invalide. Choisissez entre 1 et 7.")
        
        input("\n⏸️  Appuyez sur Entrée pour continuer...")
        print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Au revoir !")
    except Exception as e:
        print(f"\n❌ Erreur : {e}")
