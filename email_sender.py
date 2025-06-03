"""
Module pour l'envoi d'emails avec pièces jointes
"""

import smtplib
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from tqdm import tqdm
from config import EMAIL_CONFIG, EMAIL_TEMPLATE


class EmailSender:
    def __init__(self):
        self.config = EMAIL_CONFIG
        self.template = EMAIL_TEMPLATE
        self.server = None
    
    def connecter_serveur(self):
        """Établit la connexion avec le serveur SMTP"""
        try:
            print(f"📧 Connexion au serveur SMTP {self.config['smtp_server']}...")
            self.server = smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port'])
            self.server.starttls()
            self.server.login(self.config['expediteur'], self.config['mot_de_passe'])
            print("✅ Connexion SMTP établie avec succès")
            return True
        except Exception as e:
            print(f"❌ Erreur de connexion SMTP: {e}")
            return False
    
    def deconnecter_serveur(self):
        """Ferme la connexion SMTP"""
        if self.server:
            self.server.quit()
            print("📧 Connexion SMTP fermée")
    
    def creer_message(self, candidat_data, chemin_pdf):
        """
        Crée un message email avec pièce jointe
        
        Args:
            candidat_data (dict): Données du candidat
            chemin_pdf (str): Chemin vers le fichier PDF
            
        Returns:
            EmailMessage: Message email prêt à envoyer
        """
        message = EmailMessage()
        
        # En-têtes
        message['Subject'] = self.template['sujet']
        message['From'] = self.config['expediteur']
        message['To'] = candidat_data.get('Email', '')
        
        # Corps du message personnalisé
        corps_personnalise = self.template['corps'].format(
            nom=candidat_data.get('Nom', 'Candidat')
        )
        message.set_content(corps_personnalise)
        
        # Ajouter la pièce jointe PDF
        if chemin_pdf and os.path.exists(chemin_pdf):
            with open(chemin_pdf, 'rb') as f:
                pdf_data = f.read()
                message.add_attachment(
                    pdf_data,
                    maintype='application',
                    subtype='pdf',
                    filename=os.path.basename(chemin_pdf)
                )
        
        return message
    
    def envoyer_email(self, candidat_data, chemin_pdf):
        """
        Envoie un email à un candidat
        
        Args:
            candidat_data (dict): Données du candidat
            chemin_pdf (str): Chemin vers le fichier PDF
            
        Returns:
            bool: True si envoi réussi, False sinon
        """
        try:
            message = self.creer_message(candidat_data, chemin_pdf)
            self.server.send_message(message)
            return True
        except Exception as e:
            print(f"❌ Erreur envoi email pour {candidat_data.get('Email', 'N/A')}: {e}")
            return False
    
    def envoyer_emails_masse(self, df_candidats, chemins_pdfs, mode_test=True, nombre_test=3):
        """
        Envoie des emails en masse
        
        Args:
            df_candidats: DataFrame avec les données des candidats
            chemins_pdfs (dict): Dictionnaire {index: chemin_pdf}
            mode_test (bool): Si True, envoie seulement quelques emails de test
            nombre_test (int): Nombre d'emails à envoyer en mode test
            
        Returns:
            dict: Statistiques d'envoi
        """
        if not self.connecter_serveur():
            return {'erreur': 'Impossible de se connecter au serveur SMTP'}
        
        # Limiter le nombre d'envois en mode test
        if mode_test:
            df_candidats = df_candidats.head(nombre_test)
            print(f"🧪 Mode test activé - Envoi à {len(df_candidats)} candidats seulement")
        
        stats = {
            'total': len(df_candidats),
            'succes': 0,
            'echecs': 0,
            'erreurs': []
        }
        
        print(f"🚀 Début de l'envoi de {stats['total']} emails...")
        
        for index, row in tqdm(df_candidats.iterrows(), total=len(df_candidats), desc="Envoi emails"):
            candidat_data = row.to_dict()
            chemin_pdf = chemins_pdfs.get(index)
            
            if not chemin_pdf:
                print(f"⚠️  PDF manquant pour {candidat_data.get('Nom', 'N/A')}")
                stats['echecs'] += 1
                stats['erreurs'].append(f"PDF manquant pour {candidat_data.get('Nom', 'N/A')}")
                continue
            
            if not candidat_data.get('Email'):
                print(f"⚠️  Email manquant pour {candidat_data.get('Nom', 'N/A')}")
                stats['echecs'] += 1
                stats['erreurs'].append(f"Email manquant pour {candidat_data.get('Nom', 'N/A')}")
                continue
            
            if self.envoyer_email(candidat_data, chemin_pdf):
                stats['succes'] += 1
                print(f"✅ Email envoyé à {candidat_data.get('Nom', 'N/A')} ({candidat_data.get('Email', 'N/A')})")
            else:
                stats['echecs'] += 1
                stats['erreurs'].append(f"Échec envoi pour {candidat_data.get('Nom', 'N/A')}")
        
        self.deconnecter_serveur()
        
        print(f"\n📊 STATISTIQUES D'ENVOI:")
        print(f"   Total: {stats['total']}")
        print(f"   Succès: {stats['succes']}")
        print(f"   Échecs: {stats['echecs']}")
        
        if stats['erreurs']:
            print(f"\n❌ Erreurs rencontrées:")
            for erreur in stats['erreurs'][:10]:  # Afficher max 10 erreurs
                print(f"   - {erreur}")
            if len(stats['erreurs']) > 10:
                print(f"   ... et {len(stats['erreurs']) - 10} autres erreurs")
        
        return stats
    
    def tester_connexion(self):
        """Teste la connexion SMTP"""
        print("🔍 Test de connexion SMTP...")
        if self.connecter_serveur():
            self.deconnecter_serveur()
            print("✅ Test de connexion réussi")
            return True
        else:
            print("❌ Test de connexion échoué")
            return False
