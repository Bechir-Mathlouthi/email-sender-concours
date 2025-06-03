# Configuration pour l'envoi d'emails
# IMPORTANT: Ne jamais commiter ce fichier avec de vraies informations sensibles

# Configuration Email - Plusieurs fournisseurs supportés

# GMAIL (configuration actuelle)
EMAIL_CONFIG_GMAIL = {
    'expediteur': 'bechirmathlouthi.contact@gmail.com',
    'mot_de_passe': 'cnnf kdoc uycs vhdj',  # Mot de passe d'application
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

# MICROSOFT OUTLOOK (Outlook.com, Hotmail.com, Live.com)
EMAIL_CONFIG_MICROSOFT = {
    'expediteur': 'votre.email@outlook.com',  # Remplacez par votre email
    'mot_de_passe': 'votre_mot_de_passe',     # Votre mot de passe Outlook
    'smtp_server': 'smtp-mail.outlook.com',
    'smtp_port': 587
}

# OFFICE 365 (pour entreprises avec domaine personnalisé)
EMAIL_CONFIG_OFFICE365 = {
    'expediteur': 'rh@votre-entreprise.com',  # Email RH de l'entreprise
    'mot_de_passe': 'mot_de_passe_rh',        # Mot de passe du compte RH
    'smtp_server': 'smtp.office365.com',
    'smtp_port': 587
}

# Configuration active - CHANGEZ CETTE LIGNE selon votre fournisseur
EMAIL_CONFIG = EMAIL_CONFIG_GMAIL  # Changez en EMAIL_CONFIG_MICROSOFT ou EMAIL_CONFIG_OFFICE365

# Configuration des fichiers
FICHIER_EXCEL = 'candidats_selectionnes.xlsx'
DOSSIER_PDF = 'pdf_candidats'

# Configuration du PDF
PDF_CONFIG = {
    'titre': 'Fiche de Candidature',
    'police': 'Arial',
    'taille_police': 12,
    'logo_path': None  # Chemin vers le logo si disponible
}

# Configuration de l'email
EMAIL_TEMPLATE = {
    'sujet': 'Résultats de votre candidature - Concours',
    'corps': """Bonjour {nom},

Félicitations ! Vous avez été sélectionné(e) pour la prochaine étape du concours.

Veuillez trouver ci-joint votre fiche de candidature avec vos informations détaillées.

Nous vous contacterons prochainement pour les étapes suivantes.

Cordialement,
Le Service des Ressources Humaines"""
}

# Colonnes attendues dans le fichier Excel
COLONNES_REQUISES = [
    'Nom',
    'Prénom',
    'CIN',
    'Email',
    'Date de naissance',
    'Genre',
    'État Civil',
    'Nationalité',
    'Téléphone',
    'Adresse',
    'Gouvernorat',
    'Ville',
    'Code Postal',
    'Intitulé du Diplôme Universitaire',
    'Moyenne Diplôme',
    'Année Diplôme',
    'Spécialité du Baccalauréat',
    'Moyenne Bac',
    'Année Bac',
    'Session d\'Obtention du Baccalauréat',
    'Référence d\'inscription',
    'Score',
    'Code Concours',
    'Spécialité',
    'Niveau',
    'Lieu d\'affectation'
]

# Configuration pour les tests
MODE_TEST = True  # Mettre à False pour l'envoi réel
NOMBRE_TEST = 1   # Nombre d'emails à envoyer en mode test
