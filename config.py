# Configuration pour l'envoi d'emails
# IMPORTANT: Ne jamais commiter ce fichier avec de vraies informations sensibles

# Configuration Email
EMAIL_CONFIG = {
    'expediteur': 'bechirmathlouthi.contact@gmail.com',
    'mot_de_passe': 'cnnf kdoc uycs vhdj',  # Mot de passe d'application
    'smtp_server': 'smtp.gmail.com',  # Pour Gmail
    'smtp_port': 587
}

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
