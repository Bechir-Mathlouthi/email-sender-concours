"""
Module pour générer des PDFs personnalisés pour chaque candidat
"""

import os
from fpdf import FPDF
from datetime import datetime
from config import PDF_CONFIG, DOSSIER_PDF


class CandidatPDFGenerator:
    def __init__(self):
        self.dossier_pdf = DOSSIER_PDF
        self.config = PDF_CONFIG
        
        # Créer le dossier PDF s'il n'existe pas
        os.makedirs(self.dossier_pdf, exist_ok=True)
    
    def generer_pdf_candidat(self, candidat_data):
        """
        Génère un PDF pour un candidat donné
        
        Args:
            candidat_data (dict): Dictionnaire contenant les données du candidat
            
        Returns:
            str: Chemin vers le fichier PDF généré
        """
        pdf = FPDF()
        pdf.add_page()
        
        # Configuration de la police
        pdf.set_font(self.config['police'], size=self.config['taille_police'])
        
        # Titre principal centré
        self._ajouter_titre_principal(pdf)

        # Tableau des détails d'inscription (ordre exact spécifié)
        self._ajouter_tableau_inscription(pdf, candidat_data)
        
        # Pied de page
        self._ajouter_pied_page(pdf)
        
        # Sauvegarder le PDF
        nom_fichier = self._generer_nom_fichier(candidat_data)
        chemin_pdf = os.path.join(self.dossier_pdf, nom_fichier)
        pdf.output(chemin_pdf)
        
        return chemin_pdf
    
    def _ajouter_titre_principal(self, pdf):
        """Ajoute le titre principal centré"""
        pdf.set_font(self.config['police'], 'B', 16)
        pdf.cell(0, 15, "Détails de votre Inscription", ln=True, align='C')
        pdf.ln(5)
    


    def _ajouter_tableau_inscription(self, pdf, candidat_data):
        """Ajoute le tableau des détails d'inscription dans l'ordre exact spécifié"""
        # Informations d'inscription dans l'ordre EXACT spécifié par l'utilisateur
        infos_inscription = [
            ("Référence d'inscription", candidat_data.get('Référence d\'inscription', 'N/A')),
            ("Score", candidat_data.get('Score', 'N/A')),
            ("Code Concours", candidat_data.get('Code Concours', 'N/A')),
            ("Spécialité", candidat_data.get('Spécialité', 'N/A')),
            ("Niveau", candidat_data.get('Niveau', 'N/A')),
            ("Lieu d'affectation", candidat_data.get('Lieu d\'affectation', 'N/A')),
            ("Nom", candidat_data.get('Nom', 'N/A')),
            ("Prénom", candidat_data.get('Prénom', 'N/A')),
            ("CIN", candidat_data.get('CIN', 'N/A')),
            ("Date de naissance", candidat_data.get('Date de naissance', 'N/A')),
            ("Genre", candidat_data.get('Genre', 'N/A')),
            ("État Civil", candidat_data.get('État Civil', 'N/A')),
            ("Nationalité", candidat_data.get('Nationalité', 'N/A')),
            ("Email", candidat_data.get('Email', 'N/A')),
            ("Téléphone", candidat_data.get('Téléphone', 'N/A')),
            ("Adresse", candidat_data.get('Adresse', 'N/A')),
            ("Gouvernorat", candidat_data.get('Gouvernorat', 'N/A')),
            ("Ville", candidat_data.get('Ville', 'N/A')),
            ("Code Postal", candidat_data.get('Code Postal', 'N/A')),
            ("Intitulé du Diplôme Universitaire", candidat_data.get('Intitulé du Diplôme Universitaire', 'N/A')),
            ("Moyenne Diplôme", candidat_data.get('Moyenne Diplôme', 'N/A')),
            ("Année Diplôme", candidat_data.get('Année Diplôme', 'N/A')),
            ("Spécialité du Baccalauréat", candidat_data.get('Spécialité du Baccalauréat', 'N/A')),
            ("Moyenne Bac", candidat_data.get('Moyenne Bac', 'N/A')),
            ("Année Bac", candidat_data.get('Année Bac', 'N/A')),
            ("Session d'Obtention du Baccalauréat", candidat_data.get('Session d\'Obtention du Baccalauréat', 'N/A'))
        ]

        # Créer le tableau avec bordures (identique au format original)
        pdf.set_font(self.config['police'], '', 10)

        for label, valeur in infos_inscription:
            # Cellule de gauche (label) avec fond gris
            pdf.set_fill_color(240, 240, 240)  # Gris clair
            pdf.cell(70, 8, str(label), 1, 0, 'L', True)

            # Cellule de droite (valeur) sans fond
            pdf.set_fill_color(255, 255, 255)  # Blanc
            pdf.cell(120, 8, str(valeur), 1, 1, 'L', True)

        pdf.ln(5)


    
    def _ajouter_pied_page(self, pdf):
        """Ajoute le pied de page"""
        pdf.ln(10)
        pdf.set_font(self.config['police'], 'I', 8)
        pdf.cell(0, 5, f"Document généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}", ln=True, align='C')
        pdf.cell(0, 5, "Service des Ressources Humaines", ln=True, align='C')
    
    def _generer_nom_fichier(self, candidat_data):
        """Génère un nom de fichier unique pour le PDF"""
        nom = candidat_data.get('Nom', 'candidat').replace(' ', '_')
        cin = candidat_data.get('CIN', 'unknown')
        return f"candidature_{nom}_{cin}.pdf"
    
    def generer_tous_les_pdfs(self, df_candidats):
        """
        Génère tous les PDFs pour une liste de candidats
        
        Args:
            df_candidats: DataFrame pandas avec les données des candidats
            
        Returns:
            dict: Dictionnaire {index: chemin_pdf}
        """
        chemins_pdfs = {}
        
        print(f"📄 Génération de {len(df_candidats)} PDFs...")
        
        for index, row in df_candidats.iterrows():
            try:
                chemin_pdf = self.generer_pdf_candidat(row.to_dict())
                chemins_pdfs[index] = chemin_pdf
                print(f"✅ PDF généré pour {row.get('Nom', 'N/A')}")
            except Exception as e:
                print(f"❌ Erreur lors de la génération du PDF pour {row.get('Nom', 'N/A')}: {e}")
                chemins_pdfs[index] = None
        
        print(f"✅ {len([p for p in chemins_pdfs.values() if p])} PDFs générés avec succès")
        return chemins_pdfs
