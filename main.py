"""
Script principal pour l'envoi d'emails personnalisés avec PDFs aux candidats sélectionnés
"""

import pandas as pd
import os
import sys
from pdf_generator import CandidatPDFGenerator
from email_sender import EmailSender
from config import (
    FICHIER_EXCEL, 
    COLONNES_REQUISES, 
    MODE_TEST, 
    NOMBRE_TEST,
    EMAIL_CONFIG
)


def verifier_fichier_excel():
    """Vérifie que le fichier Excel existe et contient les bonnes colonnes"""
    if not os.path.exists(FICHIER_EXCEL):
        print(f"❌ Fichier Excel non trouvé: {FICHIER_EXCEL}")
        print("📝 Créez le fichier avec les colonnes suivantes:")
        for col in COLONNES_REQUISES:
            print(f"   - {col}")
        return False
    
    try:
        df = pd.read_excel(FICHIER_EXCEL)
        print(f"✅ Fichier Excel trouvé: {len(df)} candidats")
        
        # Vérifier les colonnes
        colonnes_manquantes = [col for col in COLONNES_REQUISES if col not in df.columns]
        if colonnes_manquantes:
            print(f"❌ Colonnes manquantes dans le fichier Excel:")
            for col in colonnes_manquantes:
                print(f"   - {col}")
            print(f"\n📋 Colonnes présentes: {list(df.columns)}")
            return False
        
        print(f"✅ Toutes les colonnes requises sont présentes")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier Excel: {e}")
        return False


def verifier_configuration():
    """Vérifie la configuration email"""
    if EMAIL_CONFIG['expediteur'] == 'votre.email@example.com':
        print("❌ Configuration email non modifiée!")
        print("📝 Modifiez le fichier config.py avec vos vraies informations:")
        print("   - EMAIL_CONFIG['expediteur']")
        print("   - EMAIL_CONFIG['mot_de_passe']")
        print("   - EMAIL_CONFIG['smtp_server'] (si nécessaire)")
        return False
    
    print("✅ Configuration email détectée")
    return True


def afficher_resume(df):
    """Affiche un résumé des données"""
    print(f"\n📊 RÉSUMÉ DES DONNÉES:")
    print(f"   Nombre total de candidats: {len(df)}")
    print(f"   Spécialités représentées: {df['Spécialité'].nunique()}")
    print(f"   Score moyen: {df['Score'].mean():.1f}")
    print(f"   Score min/max: {df['Score'].min()}/{df['Score'].max()}")
    
    # Vérifier les emails manquants
    emails_manquants = df['Email'].isna().sum()
    if emails_manquants > 0:
        print(f"   ⚠️  Emails manquants: {emails_manquants}")
    
    print(f"\n📋 Aperçu des premières lignes:")
    print(df[['Nom', 'Email', 'Spécialité', 'Score']].head())


def main():
    """Fonction principale"""
    print("🎯 SYSTÈME D'ENVOI D'EMAILS PERSONNALISÉS POUR CONCOURS")
    print("=" * 60)
    
    # Vérifications préliminaires
    if not verifier_fichier_excel():
        return
    
    if not verifier_configuration():
        return
    
    # Charger les données
    try:
        df = pd.read_excel(FICHIER_EXCEL)
        print(f"📊 Données chargées: {len(df)} candidats")
    except Exception as e:
        print(f"❌ Erreur lors du chargement des données: {e}")
        return
    
    # Afficher le résumé
    afficher_resume(df)
    
    # Demander confirmation
    if MODE_TEST:
        print(f"\n🧪 MODE TEST ACTIVÉ - Seulement {NOMBRE_TEST} emails seront envoyés")
    else:
        print(f"\n⚠️  MODE PRODUCTION - {len(df)} emails seront envoyés")
    
    reponse = input("\n❓ Voulez-vous continuer? (oui/non): ").lower().strip()
    if reponse not in ['oui', 'o', 'yes', 'y']:
        print("❌ Opération annulée")
        return
    
    # Étape 1: Générer les PDFs
    print(f"\n🔄 ÉTAPE 1: GÉNÉRATION DES PDFs")
    print("-" * 40)
    
    pdf_generator = CandidatPDFGenerator()
    chemins_pdfs = pdf_generator.generer_tous_les_pdfs(df)
    
    pdfs_generes = len([p for p in chemins_pdfs.values() if p])
    if pdfs_generes == 0:
        print("❌ Aucun PDF généré. Arrêt du processus.")
        return
    
    print(f"✅ {pdfs_generes} PDFs générés avec succès")
    
    # Étape 2: Tester la connexion email
    print(f"\n🔄 ÉTAPE 2: TEST DE CONNEXION EMAIL")
    print("-" * 40)
    
    email_sender = EmailSender()
    if not email_sender.tester_connexion():
        print("❌ Impossible de se connecter au serveur email. Vérifiez votre configuration.")
        return
    
    # Étape 3: Envoyer les emails
    print(f"\n🔄 ÉTAPE 3: ENVOI DES EMAILS")
    print("-" * 40)
    
    stats = email_sender.envoyer_emails_masse(
        df, 
        chemins_pdfs, 
        mode_test=MODE_TEST, 
        nombre_test=NOMBRE_TEST
    )
    
    # Résumé final
    print(f"\n🎉 PROCESSUS TERMINÉ")
    print("=" * 60)
    print(f"📊 Résultats:")
    print(f"   Total traité: {stats['total']}")
    print(f"   Emails envoyés: {stats['succes']}")
    print(f"   Échecs: {stats['echecs']}")
    
    if stats['succes'] > 0:
        print(f"\n✅ {stats['succes']} candidats ont reçu leur email avec succès!")
    
    if stats['echecs'] > 0:
        print(f"\n⚠️  {stats['echecs']} emails n'ont pas pu être envoyés.")
        print("📝 Vérifiez les erreurs ci-dessus pour plus de détails.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Processus interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
        print("📝 Vérifiez votre configuration et vos données")
