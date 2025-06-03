# 🖥️ Guide d'Utilisation - Interface Graphique

## 🎯 **NOUVELLE INTERFACE GRAPHIQUE CRÉÉE !**

Vous disposez maintenant d'une **interface graphique moderne** pour suivre l'envoi de vos emails en temps réel !

## 🚀 **Lancement de l'Interface**

### Option 1 : Double-clic (Recommandé)
```
Double-cliquez sur : interface_graphique.bat
```

### Option 2 : Ligne de commande
```bash
python lancer_interface.py
```

## 📊 **Fonctionnalités de l'Interface**

### 1. **📊 Section Informations du Fichier**
- **Fichier actuel** : Affiche le fichier Excel chargé
- **Nombre de candidats** : Total des candidats
- **Spécialités** : Nombre de spécialités différentes
- **Score moyen** : Moyenne des scores
- **Bouton "Charger fichier"** : Pour changer de fichier Excel

### 2. **⚙️ Section Configuration**
- **Mode Test** : Cochez pour envoyer seulement quelques emails de test
- **Nombre d'emails de test** : Choisissez combien d'emails de test envoyer
- **Email expéditeur** : Affiche votre email configuré

### 3. **📈 Section Progression**
- **Barre de progression** : Progression visuelle en temps réel
- **Statistiques** : Total, Succès, Échecs en temps réel
- **Temps estimé** : Temps restant estimé

### 4. **📝 Section Logs en Temps Réel**
- **Messages colorés** : 
  - 🔵 **Bleu** : Informations
  - 🟢 **Vert** : Succès
  - 🔴 **Rouge** : Erreurs
  - 🟡 **Jaune** : Avertissements
- **Horodatage** : Chaque message avec l'heure exacte
- **Défilement automatique** : Suit automatiquement les nouveaux messages

### 5. **🎛️ Section Boutons d'Action**
- **🧪 Tester la Connexion** : Teste votre connexion email
- **📄 Générer les PDFs** : Génère tous les PDFs des candidats
- **🚀 Envoyer les Emails** : Lance l'envoi des emails
- **⏹️ Arrêter** : Arrête l'envoi en cours

## 📋 **Procédure d'Utilisation**

### Étape 1 : Vérification
1. **Lancez l'interface** avec `interface_graphique.bat`
2. **Vérifiez les informations** du fichier dans la section du haut
3. **Configurez le mode** (Test ou Production)

### Étape 2 : Test de Connexion
1. **Cliquez sur "🧪 Tester la Connexion"**
2. **Attendez la confirmation** dans les logs
3. **Vérifiez** que le message "Connexion SMTP réussie !" apparaît

### Étape 3 : Génération des PDFs
1. **Cliquez sur "📄 Générer les PDFs"**
2. **Suivez la progression** dans les logs
3. **Attendez** le message de confirmation

### Étape 4 : Envoi des Emails
1. **Cliquez sur "🚀 Envoyer les Emails"**
2. **Confirmez** dans la boîte de dialogue
3. **Suivez la progression** en temps réel :
   - Barre de progression
   - Statistiques mises à jour
   - Logs détaillés pour chaque email

### Étape 5 : Suivi en Temps Réel
- **Progression visuelle** : La barre se remplit au fur et à mesure
- **Statistiques live** : Nombre de succès/échecs en temps réel
- **Logs détaillés** : Chaque email envoyé apparaît dans les logs
- **Possibilité d'arrêt** : Bouton "Arrêter" pour stopper l'envoi

## 🎨 **Avantages de l'Interface Graphique**

### ✅ **Suivi Visuel**
- **Barre de progression** pour voir l'avancement
- **Statistiques en temps réel** (succès/échecs)
- **Logs colorés** pour identifier rapidement les problèmes

### ✅ **Contrôle Total**
- **Mode test/production** facilement modifiable
- **Arrêt d'urgence** possible à tout moment
- **Chargement de différents fichiers** Excel

### ✅ **Informations Détaillées**
- **Chaque email envoyé** est loggé avec l'heure
- **Erreurs détaillées** pour diagnostic
- **Statistiques finales** complètes

### ✅ **Interface Professionnelle**
- **Design moderne** et intuitif
- **Messages d'état** clairs
- **Confirmations** avant actions importantes

## 🔧 **Résolution de Problèmes**

### Interface ne se lance pas
```bash
# Vérifiez les dépendances
python -c "import tkinter; print('Tkinter OK')"

# Relancez avec
python lancer_interface.py
```

### Erreur de connexion
- **Vérifiez** votre configuration dans `config.py`
- **Testez** avec le bouton "Tester la Connexion"
- **Consultez** les logs pour plus de détails

### PDFs non générés
- **Vérifiez** les permissions du dossier `pdf_candidats`
- **Fermez** tous les lecteurs PDF ouverts
- **Relancez** la génération

## 📊 **Exemple d'Utilisation**

1. **Lancez** : `interface_graphique.bat`
2. **Mode Test** : Coché, 3 emails
3. **Testez** : Cliquez "Tester la Connexion" → ✅ Succès
4. **Générez** : Cliquez "Générer les PDFs" → ✅ 11 PDFs générés
5. **Envoyez** : Cliquez "Envoyer les Emails" → ✅ 3/3 emails envoyés

## 🎯 **Pour l'Envoi en Masse (5000+ emails)**

1. **Décochez "Mode Test"**
2. **Chargez votre fichier** avec les 5000 candidats
3. **Générez les PDFs** (peut prendre 10-15 minutes)
4. **Lancez l'envoi** et suivez la progression en temps réel
5. **Laissez tourner** (3-4 heures pour 5000 emails)

---

## 🎉 **VOTRE INTERFACE GRAPHIQUE EST PRÊTE !**

**Vous pouvez maintenant suivre l'envoi de vos emails de manière visuelle et professionnelle !**

**Lancez l'interface avec `interface_graphique.bat` et profitez du suivi en temps réel ! 🚀**
