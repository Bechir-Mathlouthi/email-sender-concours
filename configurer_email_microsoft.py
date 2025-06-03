"""
Configuration spéciale pour les emails Microsoft (Outlook/Office 365)
"""

import os
import re

def afficher_intro():
    """Affiche l'introduction pour Microsoft"""
    print("📧 CONFIGURATION EMAIL MICROSOFT")
    print("=" * 50)
    print()
    print("Ce script vous aide à configurer votre email Microsoft pour l'envoi en masse.")
    print()
    print("🔧 TYPES D'EMAILS MICROSOFT SUPPORTÉS :")
    print("1. 📧 Outlook.com (outlook.com, hotmail.com, live.com)")
    print("2. 🏢 Office 365 (email professionnel avec domaine d'entreprise)")
    print()

def choisir_type_microsoft():
    """Permet de choisir le type d'email Microsoft"""
    print("❓ Quel type d'email Microsoft utilisez-vous ?")
    print()
    print("1. 📧 Outlook.com / Hotmail.com / Live.com (personnel)")
    print("2. 🏢 Office 365 (professionnel avec domaine d'entreprise)")
    print()
    
    while True:
        choix = input("Choisissez (1 ou 2) : ").strip()
        if choix == '1':
            return 'outlook'
        elif choix == '2':
            return 'office365'
        else:
            print("❌ Choix invalide. Veuillez choisir 1 ou 2.")

def configurer_outlook():
    """Configure Outlook.com/Hotmail/Live"""
    print("\n📧 CONFIGURATION OUTLOOK.COM")
    print("=" * 40)
    print()
    print("📝 INFORMATIONS REQUISES :")
    print("- Votre adresse email complète")
    print("- Votre mot de passe Outlook")
    print()
    print("🔒 SÉCURITÉ :")
    print("- Assurez-vous que l'authentification à 2 facteurs est activée")
    print("- Utilisez un mot de passe d'application si disponible")
    print()
    
    email = input("📧 Adresse email : ").strip()
    
    # Validation de l'email
    domaines_outlook = ['outlook.com', 'hotmail.com', 'live.com', 'msn.com']
    domaine = email.split('@')[-1].lower() if '@' in email else ''
    
    if domaine not in domaines_outlook:
        print(f"⚠️  Attention : {domaine} ne semble pas être un domaine Outlook standard.")
        print(f"📝 Domaines Outlook typiques : {', '.join(domaines_outlook)}")
        continuer = input("❓ Voulez-vous continuer ? (oui/non) : ").strip().lower()
        if continuer not in ['oui', 'o', 'yes', 'y']:
            return None
    
    mot_de_passe = input("🔑 Mot de passe : ").strip()
    
    return {
        'type': 'outlook',
        'expediteur': email,
        'mot_de_passe': mot_de_passe,
        'smtp_server': 'smtp-mail.outlook.com',
        'smtp_port': 587
    }

def configurer_office365():
    """Configure Office 365"""
    print("\n🏢 CONFIGURATION OFFICE 365")
    print("=" * 40)
    print()
    print("📝 INFORMATIONS REQUISES :")
    print("- Adresse email professionnelle (ex: rh@votre-entreprise.com)")
    print("- Mot de passe du compte professionnel")
    print()
    print("🔒 SÉCURITÉ :")
    print("- Contactez votre administrateur IT si nécessaire")
    print("- Vérifiez que l'envoi SMTP est autorisé")
    print()
    
    email = input("📧 Adresse email professionnelle : ").strip()
    
    # Validation basique
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print("❌ Format d'email invalide")
        return None
    
    domaine = email.split('@')[-1].lower()
    print(f"📝 Domaine détecté : {domaine}")
    
    mot_de_passe = input("🔑 Mot de passe : ").strip()
    
    return {
        'type': 'office365',
        'expediteur': email,
        'mot_de_passe': mot_de_passe,
        'smtp_server': 'smtp.office365.com',
        'smtp_port': 587
    }

def mettre_a_jour_config(config_email):
    """Met à jour le fichier config.py"""
    try:
        # Lire le fichier actuel
        with open('config.py', 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        # Créer une sauvegarde
        with open('config_backup.py', 'w', encoding='utf-8') as f:
            f.write(contenu)
        print("✅ Sauvegarde créée : config_backup.py")
        
        # Déterminer quelle configuration utiliser
        if config_email['type'] == 'outlook':
            nouvelle_config = "EMAIL_CONFIG = EMAIL_CONFIG_MICROSOFT"
        else:  # office365
            nouvelle_config = "EMAIL_CONFIG = EMAIL_CONFIG_OFFICE365"
        
        # Mettre à jour la configuration Microsoft ou Office365
        if config_email['type'] == 'outlook':
            # Remplacer EMAIL_CONFIG_MICROSOFT
            pattern = r"EMAIL_CONFIG_MICROSOFT = \{[^}]+\}"
            replacement = f"""EMAIL_CONFIG_MICROSOFT = {{
    'expediteur': '{config_email['expediteur']}',
    'mot_de_passe': '{config_email['mot_de_passe']}',
    'smtp_server': '{config_email['smtp_server']}',
    'smtp_port': {config_email['smtp_port']}
}}"""
        else:
            # Remplacer EMAIL_CONFIG_OFFICE365
            pattern = r"EMAIL_CONFIG_OFFICE365 = \{[^}]+\}"
            replacement = f"""EMAIL_CONFIG_OFFICE365 = {{
    'expediteur': '{config_email['expediteur']}',
    'mot_de_passe': '{config_email['mot_de_passe']}',
    'smtp_server': '{config_email['smtp_server']}',
    'smtp_port': {config_email['smtp_port']}
}}"""
        
        contenu = re.sub(pattern, replacement, contenu, flags=re.DOTALL)
        
        # Mettre à jour la configuration active
        contenu = re.sub(
            r"EMAIL_CONFIG = EMAIL_CONFIG_\w+",
            nouvelle_config,
            contenu
        )
        
        # Sauvegarder
        with open('config.py', 'w', encoding='utf-8') as f:
            f.write(contenu)
        
        print("✅ Configuration mise à jour dans config.py")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour : {e}")
        return False

def tester_configuration():
    """Teste la configuration email"""
    print("\n🧪 TEST DE LA CONFIGURATION")
    print("=" * 40)
    
    try:
        from email_sender import EmailSender
        
        print("🔍 Test de connexion SMTP...")
        email_sender = EmailSender()
        
        if email_sender.tester_connexion():
            print("✅ Connexion SMTP réussie !")
            print("🎉 Votre configuration Microsoft est fonctionnelle !")
            return True
        else:
            print("❌ Échec de la connexion SMTP")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        return False

def afficher_guide_microsoft():
    """Affiche le guide spécifique à Microsoft"""
    print("\n📖 GUIDE MICROSOFT")
    print("=" * 30)
    print()
    print("🔧 PARAMÈTRES SMTP MICROSOFT :")
    print()
    print("📧 OUTLOOK.COM / HOTMAIL.COM / LIVE.COM :")
    print("   Serveur SMTP : smtp-mail.outlook.com")
    print("   Port : 587")
    print("   Sécurité : TLS")
    print()
    print("🏢 OFFICE 365 :")
    print("   Serveur SMTP : smtp.office365.com")
    print("   Port : 587")
    print("   Sécurité : TLS")
    print()
    print("🔒 SÉCURITÉ :")
    print("   - Activez l'authentification à 2 facteurs")
    print("   - Utilisez un mot de passe d'application si possible")
    print("   - Vérifiez que l'envoi SMTP est autorisé")
    print()
    print("❓ PROBLÈMES COURANTS :")
    print("   - 'Authentification échouée' → Vérifiez le mot de passe")
    print("   - 'Connexion refusée' → Vérifiez les paramètres de sécurité")
    print("   - 'SMTP non autorisé' → Contactez l'administrateur (Office 365)")

def main():
    """Fonction principale"""
    afficher_intro()
    
    # Choix du type
    type_email = choisir_type_microsoft()
    
    # Configuration selon le type
    if type_email == 'outlook':
        config = configurer_outlook()
    else:
        config = configurer_office365()
    
    if not config:
        print("❌ Configuration annulée")
        return
    
    # Affichage de la configuration
    print(f"\n✅ CONFIGURATION {config['type'].upper()}")
    print("=" * 40)
    print(f"📧 Email : {config['expediteur']}")
    print(f"🌐 Serveur SMTP : {config['smtp_server']}")
    print(f"🔌 Port : {config['smtp_port']}")
    print()
    
    # Confirmation
    confirmer = input("❓ Voulez-vous sauvegarder cette configuration ? (oui/non) : ").strip().lower()
    
    if confirmer in ['oui', 'o', 'yes', 'y']:
        if mettre_a_jour_config(config):
            print("\n🎉 Configuration Microsoft sauvegardée avec succès !")
            
            # Test optionnel
            tester = input("\n❓ Voulez-vous tester la connexion maintenant ? (oui/non) : ").strip().lower()
            if tester in ['oui', 'o', 'yes', 'y']:
                if tester_configuration():
                    print("\n🚀 Votre système est prêt pour l'envoi d'emails Microsoft !")
                else:
                    print("\n🔧 Vérifiez votre configuration et réessayez")
                    afficher_guide_microsoft()
        else:
            print("❌ Erreur lors de la sauvegarde")
    else:
        print("❌ Configuration non sauvegardée")
    
    print("\n📖 Pour plus d'aide, consultez le guide Microsoft ci-dessus")

if __name__ == "__main__":
    main()
    input("\n📝 Appuyez sur Entrée pour continuer...")
