"""
Script pour créer un fichier Excel d'exemple avec des données de test
"""

import pandas as pd
from datetime import datetime, timedelta
import random

def creer_exemple_candidats():
    """Crée un fichier Excel d'exemple avec des candidats fictifs selon la structure réelle"""

    # Données d'exemple basées sur votre PDF réel
    candidats = [
        {
            'Nom': 'OUSSA',
            'Prénom': 'OUS',
            'CIN': '02588520',
            'Email': 'oussamabarki036@gmail.com',
            'Date de naissance': '02/11/1999',
            'Genre': 'Homme',
            'État Civil': 'Célibataire',
            'Nationalité': 'Tunisienne',
            'Téléphone': '96777777',
            'Adresse': 'tunis',
            'Gouvernorat': 'Monastir',
            'Ville': 'tunis',
            'Code Postal': '2000',
            'Intitulé du Diplôme Universitaire': 'GRH',
            'Moyenne Diplôme': '10.0',
            'Année Diplôme': '2020',
            'Spécialité du Baccalauréat': 'Sciences Techniques',
            'Moyenne Bac': '10.0',
            'Année Bac': '2016',
            'Session d\'Obtention du Baccalauréat': 'Contrôle',
            'Référence d\'inscription': 'CE25-GRH-02588520',
            'Score': '51.00',
            'Code Concours': 'CE25-GRH',
            'Spécialité': 'Gestion',
            'Niveau': 'Licence en Gestion des Ressources Humaines',
            'Lieu d\'affectation': 'Siège à Tunis'
        }
    ]

    # Ajouter quelques candidats supplémentaires avec des variations
    noms_prenoms = [
        ("AHMED", "Ahmed"), ("SALMA", "Salma"), ("MOHAMED", "Mohamed"),
        ("FATIMA", "Fatima"), ("YOUSSEF", "Youssef"), ("AMINA", "Amina"),
        ("KARIM", "Karim"), ("LEILA", "Leila"), ("OMAR", "Omar"), ("NADIA", "Nadia")
    ]

    specialites = ["Gestion", "Informatique", "Économie", "Droit", "Finance"]
    niveaux = [
        "Licence en Gestion des Ressources Humaines",
        "Licence en Informatique de Gestion",
        "Licence en Économie",
        "Licence en Droit des Affaires",
        "Licence en Finance"
    ]

    for i, (nom, prenom) in enumerate(noms_prenoms):
        candidat = {
            'Nom': nom,
            'Prénom': prenom,
            'CIN': f"0{random.randint(1000000, 9999999)}",
            'Email': f"{prenom.lower()}.{nom.lower()}@email.com",
            'Date de naissance': f"{random.randint(1, 28):02d}/{random.randint(1, 12):02d}/{random.randint(1995, 2002)}",
            'Genre': random.choice(['Homme', 'Femme']),
            'État Civil': random.choice(['Célibataire', 'Marié(e)']),
            'Nationalité': 'Tunisienne',
            'Téléphone': f"{random.randint(20000000, 99999999)}",
            'Adresse': random.choice(['Tunis', 'Sfax', 'Sousse', 'Monastir', 'Nabeul']),
            'Gouvernorat': random.choice(['Tunis', 'Sfax', 'Sousse', 'Monastir', 'Nabeul']),
            'Ville': random.choice(['Tunis', 'Sfax', 'Sousse', 'Monastir', 'Nabeul']),
            'Code Postal': f"{random.randint(1000, 9999)}",
            'Intitulé du Diplôme Universitaire': random.choice(['GRH', 'IG', 'ECO', 'DROIT', 'FIN']),
            'Moyenne Diplôme': f"{random.uniform(10.0, 18.0):.1f}",
            'Année Diplôme': f"{random.randint(2018, 2023)}",
            'Spécialité du Baccalauréat': random.choice(['Sciences Techniques', 'Sciences Expérimentales', 'Mathématiques', 'Économie']),
            'Moyenne Bac': f"{random.uniform(10.0, 18.0):.1f}",
            'Année Bac': f"{random.randint(2013, 2019)}",
            'Session d\'Obtention du Baccalauréat': random.choice(['Principale', 'Contrôle']),
            'Référence d\'inscription': f"CE25-{random.choice(['GRH', 'IG', 'ECO', 'DROIT', 'FIN'])}-0{random.randint(1000000, 9999999)}",
            'Score': f"{random.uniform(50.0, 95.0):.2f}",
            'Code Concours': f"CE25-{random.choice(['GRH', 'IG', 'ECO', 'DROIT', 'FIN'])}",
            'Spécialité': random.choice(specialites),
            'Niveau': random.choice(niveaux),
            'Lieu d\'affectation': random.choice(['Siège à Tunis', 'Antenne de Sfax', 'Antenne de Sousse'])
        }
        candidats.append(candidat)
    
    # Créer le DataFrame
    df = pd.DataFrame(candidats)
    
    # Sauvegarder en Excel
    nom_fichier = 'candidats_selectionnes_exemple.xlsx'
    df.to_excel(nom_fichier, index=False)
    
    print(f"✅ Fichier d'exemple créé: {nom_fichier}")
    print(f"📊 Contient {len(df)} candidats fictifs")
    print(f"📋 Colonnes: {list(df.columns)}")
    print(f"\n📝 Aperçu des données:")
    print(df[['Nom', 'Email', 'Spécialité', 'Score']].head())
    
    return nom_fichier

if __name__ == "__main__":
    creer_exemple_candidats()
