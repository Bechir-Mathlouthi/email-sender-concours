# 🚀 Guide Complet d'Exécution du Projet

## 📁 **FICHIERS PRINCIPAUX CRÉÉS**

### **🎯 Exécution du Projet**
- `interface_graphique.bat` - **Interface graphique (RECOMMANDÉ)**
- `demarrer.bat` - Menu principal
- `main.py` - Envoi direct en ligne de commande

### **✉️ Personnalisation des Emails**
- `changer_template.bat` - **Changement facile de template**
- `exemples_templates_email.py` - 9 templates prêts à utiliser
- `config.py` - Configuration principale

### **📊 Données et Configuration**
- `candidats_selectionnes.xlsx` - Vos données (à remplacer)
- `config.py` - Configuration email et mode test/production

## 🚀 **COMMENT EXÉCUTER LE PROJET**

### **Option 1 : Interface Graphique (RECOMMANDÉE)**
```bash
Double-cliquez sur : interface_graphique.bat
```

**Avantages :**
- ✅ Suivi visuel en temps réel
- ✅ Barre de progression animée
- ✅ Logs colorés avec horodatage
- ✅ Bouton d'arrêt fonctionnel (0.1-0.5s)
- ✅ Statistiques live (succès/échecs)
- ✅ Interface professionnelle

**Utilisation :**
1. **Vérifiez** les informations du fichier Excel
2. **Testez** la connexion email
3. **Générez** les PDFs
4. **Envoyez** les emails
5. **Suivez** la progression en direct

### **Option 2 : Menu Principal**
```bash
Double-cliquez sur : demarrer.bat
```

**Options disponibles :**
1. Configurer l'email
2. Tester le système
3. Créer un fichier Excel d'exemple
4. Interface Graphique
5. Envoi en ligne de commande
6. Afficher le guide

### **Option 3 : Ligne de Commande Directe**
```bash
python main.py          # Envoi direct
python test_system.py   # Tests du système
```

## ✉️ **COMMENT CHANGER LE CONTENU DES EMAILS**

### **Méthode 1 : Changement Facile (RECOMMANDÉ)**
```bash
Double-cliquez sur : changer_template.bat
```

**9 templates prêts à utiliser :**
1. **Template Actuel** - Par défaut
2. **Template Professionnel** - Formel et officiel
3. **Template Moderne** - Avec emojis 🎉
4. **Template avec Instructions** - Étapes détaillées
5. **Template Convocation** - Pour entretiens
6. **Template avec Score** - Inclut le score du candidat
7. **Template Admission Définitive** - Pour admission finale
8. **Template Liste d'Attente** - Pour candidats en attente
9. **Template Bilingue** - Français/Arabe

### **Méthode 2 : Modification Manuelle**
1. **Ouvrez** `config.py`
2. **Trouvez** la section `EMAIL_TEMPLATE`
3. **Modifiez** le sujet et le corps
4. **Sauvegardez** le fichier

**Exemple :**
```python
EMAIL_TEMPLATE = {
    'sujet': 'Votre nouveau sujet ici',
    'corps': """Bonjour {nom},

Votre message personnalisé...

Cordialement,
Votre signature"""
}
```

## 📋 **ÉTAPES COMPLÈTES D'UTILISATION**

### **1. Préparation des Données**
1. **Ouvrez** `candidats_selectionnes.xlsx`
2. **Remplacez** par vos vraies données (5000+ candidats)
3. **Vérifiez** que toutes les colonnes sont présentes

### **2. Personnalisation de l'Email (Optionnel)**
```bash
Double-cliquez sur : changer_template.bat
```
- Choisissez un template parmi les 9 disponibles
- Prévisualisez avant d'appliquer

### **3. Configuration du Mode**
**Pour un test (recommandé d'abord) :**
- Dans `config.py` : `MODE_TEST = True`
- `NOMBRE_TEST = 3`

**Pour l'envoi en masse :**
- Dans `config.py` : `MODE_TEST = False`

### **4. Exécution**
```bash
Double-cliquez sur : interface_graphique.bat
```

1. **Testez** la connexion email
2. **Générez** les PDFs (10-15 min pour 5000)
3. **Envoyez** les emails (3-4h pour 5000)
4. **Suivez** en temps réel

## 📊 **FORMATS DE PDF GÉNÉRÉS**

**Structure actuelle :**
1. **Titre centré** : "Détails de votre Inscription"
2. **Tableau complet** avec 26 informations dans l'ordre exact :
   - Référence d'inscription, Score, Code Concours
   - Spécialité, Niveau, Lieu d'affectation
   - Nom, Prénom, CIN, Date de naissance
   - Genre, État Civil, Nationalité, Email, Téléphone
   - Adresse, Gouvernorat, Ville, Code Postal
   - Diplôme universitaire (intitulé, moyenne, année)
   - Baccalauréat (spécialité, moyenne, année, session)
3. **Pied de page** : Date + Service RH

## 🎯 **EXEMPLES DE TEMPLATES D'EMAIL**

### **Template Professionnel**
```
Sujet: Admission - Concours de Recrutement 2025

Madame, Monsieur {nom},

Nous avons l'honneur de vous informer que votre candidature a été retenue...
```

### **Template Moderne**
```
Sujet: 🎉 Félicitations {nom} - Vous êtes sélectionné(e) !

Bonjour {nom},

🎊 Excellente nouvelle ! Votre candidature a été retenue !
📄 Votre dossier complet est en pièce jointe...
```

### **Template avec Instructions**
```
Sujet: Admission confirmée - Prochaines étapes à suivre

Cher(e) {nom},

📋 PROCHAINES ÉTAPES :
1. Consultez votre fiche en pièce jointe
2. Préparez les documents originaux...
```

## 🔧 **CONFIGURATION AVANCÉE**

### **Variables Disponibles dans les Templates**
- `{nom}` - Nom du candidat (automatique)

### **Ajout de Variables Personnalisées**
Modifiez `email_sender.py` pour ajouter :
- `{score}` - Score du candidat
- `{specialite}` - Spécialité
- `{reference}` - Référence d'inscription

## 📞 **SUPPORT ET DÉPANNAGE**

### **Problèmes Courants**
1. **Email ne s'envoie pas** → Testez avec `python test_system.py`
2. **PDF non généré** → Vérifiez les permissions du dossier
3. **Interface ne se lance pas** → Vérifiez les dépendances

### **Fichiers de Sauvegarde**
- `config_backup.py` - Sauvegarde automatique lors du changement de template
- `pdf_candidats/` - Dossier avec tous les PDFs générés

## 🎉 **RÉSUMÉ DES COMMANDES RAPIDES**

```bash
# Interface graphique (recommandé)
interface_graphique.bat

# Changer le template d'email
changer_template.bat

# Menu principal
demarrer.bat

# Test du système
python test_system.py

# Envoi direct
python main.py
```

## 📈 **CAPACITÉS DU SYSTÈME**

- ✅ **5000+ emails** supportés
- ✅ **Interface graphique** moderne
- ✅ **9 templates** d'emails prêts
- ✅ **PDFs professionnels** (format exact)
- ✅ **Suivi temps réel** avec statistiques
- ✅ **Arrêt d'urgence** fonctionnel
- ✅ **Mode test** sécurisé
- ✅ **Sauvegarde automatique** des configurations

**Votre système est maintenant complet et prêt pour l'envoi en masse ! 🚀**
