"""
Script pour changer facilement le template d'email
"""

import os
import shutil
from exemples_templates_email import *

def afficher_templates():
    """Affiche la liste des templates disponibles"""
    templates = {
        '1': ('Template Actuel (par défaut)', TEMPLATE_ACTUEL),
        '2': ('Template Professionnel', TEMPLATE_PROFESSIONNEL),
        '3': ('Template Moderne', TEMPLATE_MODERNE),
        '4': ('Template avec Instructions', TEMPLATE_AVEC_INSTRUCTIONS),
        '5': ('Template Convocation', TEMPLATE_CONVOCATION),
        '6': ('Template avec Score', TEMPLATE_AVEC_SCORE),
        '7': ('Template Admission Définitive', TEMPLATE_ADMISSION_DEFINITIVE),
        '8': ('Template Liste d\'Attente', TEMPLATE_LISTE_ATTENTE),
        '9': ('Template Bilingue', TEMPLATE_BILINGUE)
    }
    
    print("📧 CHANGEMENT DE TEMPLATE D'EMAIL")
    print("=" * 50)
    print("\nTemplates disponibles :")
    
    for num, (nom, template) in templates.items():
        print(f"{num}. {nom}")
        print(f"   Sujet: {template['sujet']}")
        print(f"   Aperçu: {template['corps'][:60]}...")
        print()
    
    return templates

def sauvegarder_config(template_choisi):
    """Sauvegarde le nouveau template dans config.py"""
    
    # Lire le fichier config.py actuel
    with open('config.py', 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    # Créer une sauvegarde
    shutil.copy('config.py', 'config_backup.py')
    print("✅ Sauvegarde créée : config_backup.py")
    
    # Trouver et remplacer la section EMAIL_TEMPLATE
    debut_template = contenu.find('EMAIL_TEMPLATE = {')
    if debut_template == -1:
        print("❌ Section EMAIL_TEMPLATE non trouvée dans config.py")
        return False
    
    # Trouver la fin de la section EMAIL_TEMPLATE
    fin_template = contenu.find('}', debut_template)
    if fin_template == -1:
        print("❌ Fin de la section EMAIL_TEMPLATE non trouvée")
        return False
    
    # Trouver la vraie fin (après le corps du message)
    compteur_accolades = 0
    pos = debut_template
    while pos < len(contenu):
        if contenu[pos] == '{':
            compteur_accolades += 1
        elif contenu[pos] == '}':
            compteur_accolades -= 1
            if compteur_accolades == 0:
                fin_template = pos
                break
        pos += 1
    
    # Créer le nouveau template
    nouveau_template = f"""EMAIL_TEMPLATE = {{
    'sujet': '{template_choisi['sujet']}',
    'corps': '''{template_choisi['corps']}'''
}}"""
    
    # Remplacer dans le contenu
    nouveau_contenu = (contenu[:debut_template] + 
                      nouveau_template + 
                      contenu[fin_template + 1:])
    
    # Sauvegarder le nouveau fichier
    with open('config.py', 'w', encoding='utf-8') as f:
        f.write(nouveau_contenu)
    
    print("✅ Template mis à jour dans config.py")
    return True

def previsualiser_template(template):
    """Affiche un aperçu du template"""
    print("\n" + "="*60)
    print("📧 APERÇU DU TEMPLATE")
    print("="*60)
    print(f"📋 Sujet: {template['sujet']}")
    print("\n📝 Corps du message:")
    print("-" * 40)
    # Remplacer {nom} par un exemple
    corps_exemple = template['corps'].replace('{nom}', 'Ahmed BENALI')
    print(corps_exemple)
    print("-" * 40)
    print()

def main():
    """Fonction principale"""
    templates = afficher_templates()
    
    while True:
        choix = input("❓ Choisissez un template (1-9) ou 'q' pour quitter : ").strip()
        
        if choix.lower() == 'q':
            print("👋 Au revoir !")
            break
        
        if choix not in templates:
            print("❌ Choix invalide. Veuillez choisir entre 1 et 9.")
            continue
        
        nom_template, template_choisi = templates[choix]
        
        print(f"\n✅ Template sélectionné : {nom_template}")
        
        # Prévisualisation
        previsualiser_template(template_choisi)
        
        # Confirmation
        confirmer = input("❓ Voulez-vous appliquer ce template ? (oui/non) : ").strip().lower()
        
        if confirmer in ['oui', 'o', 'yes', 'y']:
            if sauvegarder_config(template_choisi):
                print("\n🎉 Template appliqué avec succès !")
                print("📝 Vous pouvez maintenant tester avec MODE_TEST = True")
                print("📧 Lancez python main.py ou l'interface graphique pour tester")
            else:
                print("\n❌ Erreur lors de l'application du template")
                print("🔄 Restauration depuis config_backup.py...")
                try:
                    shutil.copy('config_backup.py', 'config.py')
                    print("✅ Configuration restaurée")
                except:
                    print("❌ Erreur de restauration")
        else:
            print("❌ Template non appliqué")
        
        break

def tester_template():
    """Teste le template actuel"""
    print("\n🧪 TEST DU TEMPLATE ACTUEL")
    print("=" * 40)
    
    try:
        from config import EMAIL_TEMPLATE
        print("✅ Template chargé avec succès")
        print(f"📋 Sujet: {EMAIL_TEMPLATE['sujet']}")
        print("\n📝 Corps (avec exemple):")
        corps_test = EMAIL_TEMPLATE['corps'].format(nom="Ahmed BENALI")
        print(corps_test)
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")

if __name__ == "__main__":
    print("📧 GESTIONNAIRE DE TEMPLATES D'EMAIL")
    print("=" * 50)
    print("1. Changer le template")
    print("2. Tester le template actuel")
    print("3. Quitter")
    
    choix = input("\n❓ Que voulez-vous faire ? (1-3) : ").strip()
    
    if choix == '1':
        main()
    elif choix == '2':
        tester_template()
    elif choix == '3':
        print("👋 Au revoir !")
    else:
        print("❌ Choix invalide")
        main()
