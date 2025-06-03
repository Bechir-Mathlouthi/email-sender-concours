"""
Script pour finaliser le push vers GitHub
"""

import subprocess
import sys
import os

def executer_commande(commande, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(commande, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} réussi !")
            if result.stdout.strip():
                print(f"📝 Sortie: {result.stdout.strip()}")
        else:
            print(f"❌ Erreur lors de {description}")
            print(f"📝 Erreur: {result.stderr.strip()}")
            return False
        return True
    except Exception as e:
        print(f"❌ Exception lors de {description}: {e}")
        return False

def main():
    """Fonction principale"""
    print("🚀 FINALISATION DU PUSH VERS GITHUB")
    print("=" * 50)
    
    # Vérifier si on est dans un repository git
    if not os.path.exists('.git'):
        print("❌ Pas de repository Git trouvé. Initialisation...")
        if not executer_commande("git init", "Initialisation Git"):
            return
    
    # Vérifier le statut
    print("\n📊 STATUT ACTUEL")
    executer_commande("git status --short", "Vérification du statut")
    
    # Ajouter le guide de push au commit
    print("\n📝 AJOUT DU GUIDE DE PUSH")
    executer_commande("git add GUIDE_PUSH_GITHUB.md", "Ajout du guide")
    executer_commande("git add finaliser_github.py", "Ajout du script")
    executer_commande("git add push_to_github.bat", "Ajout du script batch")
    
    # Commit des nouveaux fichiers
    executer_commande('git commit -m "📚 Ajout guides et scripts pour push GitHub"', "Commit des guides")
    
    # Afficher les informations du repository
    print("\n📋 INFORMATIONS DU REPOSITORY")
    executer_commande("git log --oneline -5", "Historique des commits")
    executer_commande("git remote -v", "Remotes configurés")
    
    # Instructions finales
    print("\n" + "="*60)
    print("🎯 ÉTAPES FINALES POUR GITHUB")
    print("="*60)
    print()
    print("1. 🌐 CRÉER LE REPOSITORY SUR GITHUB :")
    print("   - Allez sur : https://github.com/Bechir-Mathlouthi")
    print("   - Cliquez 'New repository'")
    print("   - Nom : email-sender-concours")
    print("   - Description : Système d'envoi d'emails personnalisés avec interface graphique")
    print("   - Public ou Private (au choix)")
    print("   - NE PAS cocher 'Add README' (on en a déjà un)")
    print("   - Cliquez 'Create repository'")
    print()
    print("2. 🚀 POUSSER LE CODE :")
    print("   Après création du repository, exécutez :")
    print("   git push -u origin main")
    print()
    print("   Ou utilisez le script automatique :")
    print("   push_to_github.bat")
    print()
    print("3. ✅ VÉRIFICATION :")
    print("   Votre projet sera visible à :")
    print("   https://github.com/Bechir-Mathlouthi/email-sender-concours")
    print()
    print("="*60)
    print("📊 CONTENU DU REPOSITORY :")
    print("="*60)
    
    # Lister les fichiers qui seront poussés
    try:
        result = subprocess.run("git ls-files", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            fichiers = result.stdout.strip().split('\n')
            print(f"📁 {len(fichiers)} fichiers seront poussés :")
            for i, fichier in enumerate(fichiers[:15], 1):  # Afficher les 15 premiers
                print(f"   {i:2d}. {fichier}")
            if len(fichiers) > 15:
                print(f"   ... et {len(fichiers) - 15} autres fichiers")
        else:
            print("❌ Impossible de lister les fichiers")
    except Exception as e:
        print(f"❌ Erreur lors du listage : {e}")
    
    print()
    print("🎉 VOTRE PROJET EST PRÊT POUR GITHUB !")
    print("📖 Consultez GUIDE_PUSH_GITHUB.md pour plus de détails")

if __name__ == "__main__":
    main()
    input("\n📝 Appuyez sur Entrée pour continuer...")
