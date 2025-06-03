"""
Script interactif pour configurer facilement les paramètres email
"""

import os
import re

def valider_email(email):
    """Valide le format d'un email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def configurer_email_interactif():
    """Configuration interactive des paramètres email"""
    print("🔧 CONFIGURATION INTERACTIVE DES PARAMÈTRES EMAIL")
    print("=" * 60)
    
    # Demander l'email
    while True:
        email = input("📧 Entrez votre adresse email : ").strip()
        if valider_email(email):
            break
        print("❌ Format d'email invalide. Essayez à nouveau.")
    
    # Demander le mot de passe
    print("\n🔐 Mot de passe d'application :")
    print("   Pour Gmail : https://myaccount.google.com/apppasswords")
    print("   Le mot de passe doit faire 16 caractères (ex: abcd efgh ijkl mnop)")
    
    while True:
        mot_de_passe = input("🔑 Entrez votre mot de passe d'application : ").strip()
        if len(mot_de_passe) >= 8:
            break
        print("❌ Le mot de passe semble trop court. Vérifiez qu'il s'agit bien d'un mot de passe d'application.")
    
    # Détecter le serveur SMTP
    if 'gmail.com' in email:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
    elif 'outlook.com' in email or 'hotmail.com' in email:
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
    elif 'yahoo.com' in email:
        smtp_server = 'smtp.mail.yahoo.com'
        smtp_port = 587
    else:
        print(f"\n⚠️  Serveur SMTP non détecté automatiquement pour {email}")
        smtp_server = input("📡 Entrez le serveur SMTP (ex: smtp.gmail.com) : ").strip()
        smtp_port = int(input("🔌 Entrez le port SMTP (généralement 587) : ").strip() or "587")
    
    print(f"\n📡 Serveur SMTP détecté : {smtp_server}:{smtp_port}")
    
    # Mode de fonctionnement
    print(f"\n🧪 Mode de fonctionnement :")
    print("   1. Mode TEST (recommandé) - Envoie seulement 3 emails")
    print("   2. Mode PRODUCTION - Envoie tous les emails")
    
    while True:
        choix = input("Choisissez le mode (1 ou 2) : ").strip()
        if choix in ['1', '2']:
            mode_test = choix == '1'
            break
        print("❌ Choisissez 1 ou 2")
    
    # Générer le nouveau fichier config.py
    config_content = f'''# Configuration pour l'envoi d'emails
# IMPORTANT: Ne jamais commiter ce fichier avec de vraies informations sensibles

# Configuration Email
EMAIL_CONFIG = {{
    'expediteur': '{email}',
    'mot_de_passe': '{mot_de_passe}',
    'smtp_server': '{smtp_server}',
    'smtp_port': {smtp_port}
}}

# Configuration des fichiers
FICHIER_EXCEL = 'candidats_selectionnes.xlsx'
DOSSIER_PDF = 'pdf_candidats'

# Configuration du PDF
PDF_CONFIG = {{
    'titre': 'Fiche de Candidature',
    'police': 'Arial',
    'taille_police': 12,
    'logo_path': None  # Chemin vers le logo si disponible
}}

# Configuration de l'email
EMAIL_TEMPLATE = {{
    'sujet': 'Résultats de votre candidature - Concours',
    'corps': """Bonjour {{nom}},

Félicitations ! Vous avez été sélectionné(e) pour la prochaine étape du concours.

Veuillez trouver ci-joint votre fiche de candidature avec vos informations détaillées.

Nous vous contacterons prochainement pour les étapes suivantes.

Cordialement,
Le Service des Ressources Humaines"""
}}

# Colonnes attendues dans le fichier Excel
COLONNES_REQUISES = [
    'Nom',
    'CIN', 
    'Email',
    'Date de naissance',
    'Spécialité',
    'Nationalité',
    'Score'
]

# Configuration pour les tests
MODE_TEST = {str(mode_test).lower()}  # Mettre à False pour l'envoi réel
NOMBRE_TEST = 3   # Nombre d'emails à envoyer en mode test'''
    
    # Sauvegarder la configuration
    with open('config.py', 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print(f"\n✅ Configuration sauvegardée dans config.py")
    print(f"📧 Email configuré : {email}")
    print(f"📡 Serveur SMTP : {smtp_server}:{smtp_port}")
    print(f"🧪 Mode : {'TEST' if mode_test else 'PRODUCTION'}")
    
    # Proposer de tester
    print(f"\n🔍 Voulez-vous tester la configuration maintenant ?")
    tester = input("Taper 'oui' pour tester : ").strip().lower()
    
    if tester in ['oui', 'o', 'yes', 'y']:
        print(f"\n🧪 Lancement du test...")
        os.system('python test_system.py')
    
    print(f"\n🎉 Configuration terminée !")
    print(f"📝 Prochaines étapes :")
    print(f"   1. Remplacez les données dans candidats_selectionnes.xlsx")
    print(f"   2. Lancez : python main.py")

if __name__ == "__main__":
    try:
        configurer_email_interactif()
    except KeyboardInterrupt:
        print(f"\n\n❌ Configuration annulée")
    except Exception as e:
        print(f"\n❌ Erreur : {e}")

