# 📧 Guide d'Exécution et Personnalisation du Projet

## 🚀 **COMMENT EXÉCUTER LE PROJET**

### **Option 1 : Interface Graphique (RECOMMANDÉE)**
```bash
# Double-cliquez sur le fichier :
interface_graphique.bat

# Ou via ligne de commande :
python lancer_interface.py
```

**Avantages :**
- ✅ Suivi visuel en temps réel
- ✅ Barre de progression
- ✅ Logs colorés
- ✅ Contrôle total (arrêt possible)
- ✅ Interface professionnelle

### **Option 2 : Menu Principal**
```bash
# Double-cliquez sur le fichier :
demarrer.bat

# Ou via ligne de commande :
python demarrer.py
```

### **Option 3 : Ligne de Commande Directe**
```bash
# Envoi direct
python main.py

# Tests du système
python test_system.py
```

## 📋 **ÉTAPES D'EXÉCUTION COMPLÈTE**

### **1. Préparation des Données**
1. **Ouvrez** `candidats_selectionnes.xlsx`
2. **Remplacez** le contenu par vos vraies données
3. **Vérifiez** que toutes les colonnes sont présentes :

**Colonnes requises :**
```
- Nom, Prénom, CIN, Email, Date de naissance
- Genre, État Civil, Nationalité, Téléphone
- Adresse, Gouvernorat, Ville, Code Postal
- Intitulé du Diplôme Universitaire, Moyenne Diplôme, Année Diplôme
- Spécialité du Baccalauréat, Moyenne Bac, Année Bac
- Session d'Obtention du Baccalauréat
- Référence d'inscription, Score, Code Concours
- Spécialité, Niveau, Lieu d'affectation
```

### **2. Configuration du Mode**

**Pour un test (recommandé d'abord) :**
1. **Ouvrez** `config.py`
2. **Vérifiez** : `MODE_TEST = True`
3. **Définissez** : `NOMBRE_TEST = 3` (ou le nombre souhaité)

**Pour l'envoi en masse :**
1. **Ouvrez** `config.py`
2. **Changez** : `MODE_TEST = False`

### **3. Exécution avec Interface Graphique**
1. **Lancez** `interface_graphique.bat`
2. **Vérifiez** les informations du fichier
3. **Testez** la connexion email (bouton "🧪 Tester la Connexion")
4. **Générez** les PDFs (bouton "📄 Générer les PDFs")
5. **Envoyez** les emails (bouton "🚀 Envoyer les Emails")
6. **Suivez** la progression en temps réel

### **4. Suivi de l'Envoi**
- **Barre de progression** : Avancement visuel
- **Statistiques** : Total | Succès | Échecs (mis à jour en temps réel)
- **Logs détaillés** : Chaque email avec horodatage
- **Arrêt possible** : Bouton "⏹️ Arrêter" (fonctionne en 0.1-0.5s)

## ✉️ **COMMENT CHANGER LE CORPS DE L'EMAIL**

### **Localisation du Template**
Le contenu de l'email se trouve dans le fichier `config.py` :

```python
EMAIL_TEMPLATE = {
    'sujet': 'Résultats de votre candidature - Concours',
    'corps': """Bonjour {nom},

Félicitations ! Vous avez été sélectionné(e) pour la prochaine étape du concours.

Veuillez trouver ci-joint votre fiche de candidature avec vos informations détaillées.

Nous vous contacterons prochainement pour les étapes suivantes.

Cordialement,
Le Service des Ressources Humaines"""
}
```

### **Modification du Sujet**
```python
'sujet': 'Votre nouveau sujet ici'
```

**Exemples :**
```python
'sujet': 'Félicitations - Vous êtes sélectionné(e) !'
'sujet': 'Résultats du concours 2025 - Admission'
'sujet': 'Convocation pour la prochaine étape'
```

### **Modification du Corps du Message**

**Structure actuelle :**
```python
'corps': """Bonjour {nom},

Votre message personnalisé ici...

Cordialement,
Votre signature"""
```

**Variables disponibles :**
- `{nom}` : Nom du candidat (automatiquement remplacé)

**Exemples de personnalisation :**

#### **Exemple 1 : Message de félicitations**
```python
'corps': """Cher(e) {nom},

🎉 Félicitations ! Nous avons le plaisir de vous informer que votre candidature a été retenue.

📄 Vous trouverez en pièce jointe votre fiche détaillée avec toutes vos informations.

📞 Notre équipe vous contactera dans les 48 heures pour les prochaines étapes.

Cordialement,
L'équipe de recrutement
Service des Ressources Humaines"""
```

#### **Exemple 2 : Message formel**
```python
'corps': """Madame, Monsieur {nom},

Suite à votre candidature au concours, nous vous informons que vous avez été sélectionné(e) pour poursuivre le processus.

Veuillez trouver ci-joint votre dossier de candidature complet.

Pour toute question, n'hésitez pas à nous contacter.

Salutations distinguées,
Direction des Ressources Humaines"""
```

#### **Exemple 3 : Message avec instructions**
```python
'corps': """Bonjour {nom},

Excellente nouvelle ! Vous êtes admis(e) à la prochaine phase du concours.

📋 PROCHAINES ÉTAPES :
1. Consultez votre fiche en pièce jointe
2. Préparez les documents demandés
3. Attendez notre convocation

📧 Contact : recrutement@entreprise.com
📞 Téléphone : +216 XX XXX XXX

Félicitations et à bientôt !
L'équipe RH"""
```

### **Ajout de Variables Personnalisées**

Si vous voulez ajouter d'autres variables (comme le score, la spécialité, etc.), modifiez le fichier `email_sender.py` :

**Dans la méthode `creer_message` (ligne 59) :**
```python
# Corps du message personnalisé
corps_personnalise = self.template['corps'].format(
    nom=candidat_data.get('Nom', 'Candidat'),
    score=candidat_data.get('Score', 'N/A'),
    specialite=candidat_data.get('Spécialité', 'N/A'),
    reference=candidat_data.get('Référence d\'inscription', 'N/A')
)
```

**Puis dans `config.py` :**
```python
'corps': """Bonjour {nom},

Félicitations ! Votre score de {score} vous permet d'être sélectionné(e) en {specialite}.

Référence : {reference}

Cordialement,
Le Service RH"""
```

## 🔧 **MODIFICATION ÉTAPE PAR ÉTAPE**

### **1. Ouvrir le fichier de configuration**
```bash
# Ouvrez avec un éditeur de texte :
notepad config.py
# Ou avec votre éditeur préféré
```

### **2. Localiser la section EMAIL_TEMPLATE**
```python
EMAIL_TEMPLATE = {
    'sujet': 'Résultats de votre candidature - Concours',
    'corps': """Bonjour {nom},
    ...
```

### **3. Modifier le contenu**
- **Changez** le sujet entre les guillemets
- **Modifiez** le corps entre les triple guillemets `"""`
- **Gardez** `{nom}` pour la personnalisation

### **4. Sauvegarder et tester**
1. **Sauvegardez** le fichier
2. **Lancez** un test avec `MODE_TEST = True`
3. **Vérifiez** l'email reçu
4. **Ajustez** si nécessaire

## 📧 **EXEMPLES DE TEMPLATES PRÊTS À UTILISER**

### **Template Professionnel**
```python
EMAIL_TEMPLATE = {
    'sujet': 'Admission - Concours de Recrutement 2025',
    'corps': """Madame, Monsieur {nom},

Nous avons l'honneur de vous informer que votre candidature a été retenue suite à l'examen de votre dossier.

Vous trouverez en pièce jointe votre fiche de candidature détaillée.

Nous vous contacterons prochainement pour vous communiquer les modalités de la suite du processus.

Nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.

Le Service des Ressources Humaines"""
}
```

### **Template Moderne**
```python
EMAIL_TEMPLATE = {
    'sujet': '🎉 Félicitations {nom} - Vous êtes sélectionné(e) !',
    'corps': """Bonjour {nom},

🎊 Excellente nouvelle ! Votre candidature a été retenue !

📄 Votre dossier complet est en pièce jointe
📞 Nous vous appellerons sous 48h
✨ Préparez-vous pour la suite de l'aventure !

À très bientôt,
L'équipe RH 🚀"""
}
```

## 🔄 **APRÈS MODIFICATION**

1. **Sauvegardez** `config.py`
2. **Testez** avec `MODE_TEST = True` et `NOMBRE_TEST = 1`
3. **Vérifiez** l'email reçu
4. **Ajustez** si nécessaire
5. **Passez** en mode production : `MODE_TEST = False`

## 📊 **RÉSUMÉ DES FICHIERS IMPORTANTS**

- **`config.py`** : Configuration email et template
- **`candidats_selectionnes.xlsx`** : Vos données
- **`interface_graphique.bat`** : Lancement interface
- **`email_sender.py`** : Logique d'envoi (pour modifications avancées)

**Votre système est maintenant prêt et personnalisable ! 🎯**
