# 📧 Système d'Envoi d'Emails Personnalisés pour Concours

Un système complet et professionnel pour l'envoi automatisé d'emails personnalisés avec génération de PDFs pour les résultats de concours.

## 🎯 **Fonctionnalités Principales**

- ✅ **Interface Graphique Moderne** - Suivi en temps réel avec barre de progression
- ✅ **Génération PDF Professionnelle** - Format identique aux documents officiels
- ✅ **Envoi Email en Masse** - Support de 5000+ emails
- ✅ **9 Templates d'Emails** - Prêts à utiliser et personnalisables
- ✅ **Mode Test Sécurisé** - Validation avant envoi en masse
- ✅ **Arrêt d'Urgence** - Contrôle total de l'envoi
- ✅ **Statistiques Temps Réel** - Suivi des succès/échecs

## 🚀 **Démarrage Rapide**

### **Installation**
```bash
git clone https://github.com/Bechir-Mathlouthi/email-sender-concours.git
cd email-sender-concours
pip install -r requirements.txt
```

### **Configuration**
1. **Configurez votre email** :
   ```bash
   python configurer_email.py
   ```

2. **Préparez vos données** :
   - Remplacez `candidats_selectionnes.xlsx` par vos données
   - 26 colonnes requises (voir guide)

### **Exécution**
```bash
# Interface graphique (recommandé)
interface_graphique.bat

# Ou via Python
python lancer_interface.py
```

## 📊 **Structure du Projet**

```
📁 email-sender-concours/
├── 🎯 interface_graphique.bat      # Interface principale
├── 🔧 changer_template.bat         # Changement d'email
├── 📧 config.py                    # Configuration
├── 📄 candidats_selectionnes.xlsx  # Données (à remplacer)
├── 🐍 main.py                      # Script principal
├── 🖥️ interface_graphique.py       # Interface GUI
├── 📧 email_sender.py              # Logique d'envoi
├── 📄 pdf_generator.py             # Génération PDF
├── ✉️ exemples_templates_email.py  # 9 templates prêts
└── 📋 requirements.txt             # Dépendances
```

## 🎨 **Templates d'Emails Disponibles**

1. **Template Professionnel** - Formel et officiel
2. **Template Moderne** - Avec emojis et style moderne
3. **Template avec Instructions** - Étapes détaillées
4. **Template Convocation** - Pour entretiens
5. **Template avec Score** - Inclut le score du candidat
6. **Template Admission Définitive** - Pour admission finale
7. **Template Liste d'Attente** - Pour candidats en attente
8. **Template Bilingue** - Français/Arabe
9. **Template Personnalisé** - Modifiable

## 📋 **Données Requises (Excel)**

Le fichier Excel doit contenir 26 colonnes :

**Informations Personnelles :**
- Nom, Prénom, CIN, Email, Date de naissance
- Genre, État Civil, Nationalité, Téléphone
- Adresse, Gouvernorat, Ville, Code Postal

**Informations Académiques :**
- Intitulé du Diplôme Universitaire, Moyenne Diplôme, Année Diplôme
- Spécialité du Baccalauréat, Moyenne Bac, Année Bac
- Session d'Obtention du Baccalauréat

**Informations Concours :**
- Référence d'inscription, Score, Code Concours
- Spécialité, Niveau, Lieu d'affectation

## 🖥️ **Interface Graphique**

**Fonctionnalités :**
- 📊 Informations du fichier en temps réel
- ⚙️ Configuration mode test/production
- 📈 Barre de progression animée
- 📝 Logs colorés avec horodatage
- 🛑 Arrêt d'urgence (0.1-0.5s)
- 📊 Statistiques live

## 📧 **Configuration Email**

### **Gmail (Recommandé)**
1. Activez l'authentification à 2 facteurs
2. Générez un mot de passe d'application
3. Utilisez le script de configuration :
   ```bash
   python configurer_email.py
   ```

## 🎯 **Utilisation**

### **Mode Test (Recommandé d'abord)**
```python
# Dans config.py
MODE_TEST = True
NOMBRE_TEST = 3
```

### **Mode Production**
```python
# Dans config.py
MODE_TEST = False
```

### **Changement de Template Email**
```bash
changer_template.bat
```

## 📄 **Format PDF Généré**

Les PDFs générés suivent le format officiel :
- **Titre centré** : "Détails de votre Inscription"
- **Tableau professionnel** avec bordures
- **26 informations** dans l'ordre exact
- **Pied de page** avec date et service

## 🔧 **Personnalisation**

### **Modifier le Template Email**
```python
EMAIL_TEMPLATE = {
    'sujet': 'Votre nouveau sujet',
    'corps': '''Bonjour {nom},
    
    Votre message personnalisé...
    
    Cordialement,
    Votre signature'''
}
```

## 🛠️ **Dépendances**

```
pandas>=1.5.0
fpdf2>=2.7.0
tqdm>=4.64.0
openpyxl>=3.0.0
tkinter (inclus avec Python)
```

## 📊 **Performances**

- **5000+ emails** : 3-4 heures
- **Génération PDFs** : 10-15 minutes pour 5000
- **Interface responsive** : Temps réel
- **Mémoire optimisée** : Traitement par lots

## 🎉 **Fonctionnalités Avancées**

- **Sauvegarde automatique** des configurations
- **Gestion d'erreurs** robuste
- **Logs détaillés** pour diagnostic
- **Interface multilingue** (templates)
- **Arrêt d'urgence** fonctionnel
- **Statistiques complètes**

## 🤝 **Contribution**

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ouvrir des issues
- Proposer des améliorations
- Ajouter de nouveaux templates
- Améliorer la documentation

## 📄 **Licence**

Ce projet est sous licence MIT.

## 👨‍💻 **Auteur**

**Bechir Mathlouthi**
- GitHub: [@Bechir-Mathlouthi](https://github.com/Bechir-Mathlouthi)

---

⭐ **N'oubliez pas de mettre une étoile si ce projet vous aide !**
