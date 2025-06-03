# 🔧 Guide de Configuration - Envoi d'Emails Personnalisés

## ✅ Système Installé et Prêt !

Votre système d'envoi d'emails personnalisés est maintenant installé. Voici ce qui a été créé :

### 📁 Fichiers créés :
- ✅ `main.py` - Script principal
- ✅ `config.py` - Configuration (À MODIFIER)
- ✅ `pdf_generator.py` - Génération des PDFs
- ✅ `email_sender.py` - Envoi des emails
- ✅ `test_system.py` - Tests du système
- ✅ `candidats_selectionnes.xlsx` - Fichier Excel d'exemple
- ✅ `requirements.txt` - Dépendances Python

## 🚨 ÉTAPES OBLIGATOIRES AVANT UTILISATION

### 1. Configurer votre email dans `config.py`

**IMPORTANT :** Vous devez modifier le fichier `config.py` avec vos vraies informations :

```python
EMAIL_CONFIG = {
    'expediteur': 'votre.email@gmail.com',  # ← Remplacez par votre email
    'mot_de_passe': 'votre_mot_de_passe_application',  # ← Mot de passe d'application
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}
```

### 2. Créer un mot de passe d'application Gmail

**Si vous utilisez Gmail :**

1. Allez sur votre compte Google : https://myaccount.google.com/
2. Sécurité → Validation en deux étapes (activez-la si pas déjà fait)
3. Sécurité → Mots de passe des applications
4. Sélectionnez "Autre" et tapez "Envoi emails concours"
5. Copiez le mot de passe généré (16 caractères)
6. Utilisez ce mot de passe dans `config.py`

### 3. Préparer votre fichier Excel

Remplacez le contenu de `candidats_selectionnes.xlsx` par vos vraies données.

**Colonnes obligatoires :**
- `Nom` - Nom complet du candidat
- `CIN` - Numéro de carte d'identité
- `Email` - Adresse email du candidat
- `Date de naissance` - Format YYYY-MM-DD
- `Spécialité` - Domaine d'études
- `Nationalité` - Nationalité du candidat
- `Score` - Score obtenu au concours

**Colonnes optionnelles :**
- `Diplôme`, `Université`, `Année_diplôme` (seront incluses dans le PDF si présentes)

## 🧪 TESTER LE SYSTÈME

### Étape 1 : Tester les composants
```bash
python test_system.py
```

### Étape 2 : Tester avec quelques emails
1. Assurez-vous que `MODE_TEST = True` dans `config.py`
2. Lancez : `python main.py`
3. Le système enverra seulement 3 emails de test

### Étape 3 : Envoi en production
1. Changez `MODE_TEST = False` dans `config.py`
2. Lancez : `python main.py`
3. Confirmez l'envoi des 5000+ emails

## 📊 Résultats des Tests Actuels

✅ **Génération PDF** : Fonctionne parfaitement
✅ **Création messages** : Fonctionne parfaitement
❌ **Connexion email** : Nécessite votre configuration
❌ **Lecture Excel** : Résolu (openpyxl mis à jour)

## 🔧 Configuration pour Gros Volumes (5000+ emails)

Pour éviter les limitations des serveurs email :

### Option 1 : Gmail avec délais
```python
# Dans email_sender.py, ajoutez après chaque envoi :
import time
time.sleep(2)  # Pause de 2 secondes entre chaque email
```

### Option 2 : Service professionnel
Considérez l'utilisation de :
- **SendGrid** (30 000 emails gratuits/mois)
- **Mailgun** (10 000 emails gratuits/mois)
- **Amazon SES** (très économique)

## 📝 Structure de votre fichier Excel

Voici un exemple de structure attendue :

| Nom | CIN | Email | Date de naissance | Spécialité | Nationalité | Score |
|-----|-----|-------|-------------------|------------|-------------|-------|
| Ahmed Ben Ali | 12345678 | ahmed@email.com | 1990-05-20 | Informatique | Tunisienne | 85 |
| Salma Trabelsi | 87654321 | salma@email.com | 1992-11-03 | Économie | Tunisienne | 90 |

## 🚀 Commandes Rapides

```bash
# Tester le système
python test_system.py

# Envoi en mode test (3 emails)
python main.py

# Créer un nouveau fichier d'exemple
python creer_exemple_excel.py
```

## 🆘 Dépannage

### Erreur "Username and Password not accepted"
- Vérifiez que vous utilisez un mot de passe d'application
- Assurez-vous que la validation en 2 étapes est activée

### Erreur "PDF non généré"
- Vérifiez les permissions d'écriture dans le dossier
- Assurez-vous que le dossier `pdf_candidats` existe

### Emails en spam
- Demandez aux destinataires d'ajouter votre email à leur liste blanche
- Limitez le nombre d'envois simultanés

## 📞 Prochaines Étapes

1. **Modifiez `config.py`** avec vos vraies informations
2. **Testez avec `python test_system.py`**
3. **Remplacez les données dans `candidats_selectionnes.xlsx`**
4. **Lancez un test avec 3 emails**
5. **Si tout fonctionne, lancez l'envoi complet**

---

**🎯 Votre système est prêt ! Il ne manque que votre configuration email.**
