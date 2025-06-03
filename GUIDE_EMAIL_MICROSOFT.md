# 📧 Guide Configuration Email Microsoft

## 🎯 **SUPPORT MICROSOFT AJOUTÉ !**

Votre système supporte maintenant **tous les types d'emails Microsoft** :
- ✅ **Outlook.com** (outlook.com, hotmail.com, live.com)
- ✅ **Office 365** (emails professionnels d'entreprise)

## 🚀 **CONFIGURATION RAPIDE**

### **Option 1 : Script Automatique (RECOMMANDÉ)**
```bash
python configurer_email_microsoft.py
```

### **Option 2 : Configuration Manuelle**
Modifiez directement `config.py`

## 📧 **TYPES D'EMAILS MICROSOFT**

### **1. Outlook.com / Hotmail.com / Live.com**
**Pour emails personnels Microsoft :**

```python
# Dans config.py, changez cette ligne :
EMAIL_CONFIG = EMAIL_CONFIG_MICROSOFT

# Et modifiez :
EMAIL_CONFIG_MICROSOFT = {
    'expediteur': 'votre.email@outlook.com',  # Votre email
    'mot_de_passe': 'votre_mot_de_passe',     # Votre mot de passe
    'smtp_server': 'smtp-mail.outlook.com',
    'smtp_port': 587
}
```

**Domaines supportés :**
- `@outlook.com`
- `@hotmail.com` 
- `@live.com`
- `@msn.com`

### **2. Office 365 (Entreprise)**
**Pour emails professionnels avec domaine d'entreprise :**

```python
# Dans config.py, changez cette ligne :
EMAIL_CONFIG = EMAIL_CONFIG_OFFICE365

# Et modifiez :
EMAIL_CONFIG_OFFICE365 = {
    'expediteur': 'rh@votre-entreprise.com',  # Email RH
    'mot_de_passe': 'mot_de_passe_rh',        # Mot de passe RH
    'smtp_server': 'smtp.office365.com',
    'smtp_port': 587
}
```

**Exemples d'emails Office 365 :**
- `rh@votre-entreprise.com`
- `recrutement@societe.tn`
- `admin@organisation.org`

## 🔧 **PARAMÈTRES SMTP MICROSOFT**

### **Outlook.com / Hotmail / Live**
```
Serveur SMTP : smtp-mail.outlook.com
Port : 587
Sécurité : TLS/STARTTLS
Authentification : Oui
```

### **Office 365**
```
Serveur SMTP : smtp.office365.com
Port : 587
Sécurité : TLS/STARTTLS
Authentification : Oui
```

## 🔒 **SÉCURITÉ MICROSOFT**

### **Pour Outlook.com :**
1. **Activez l'authentification à 2 facteurs**
2. **Générez un mot de passe d'application** (recommandé)
3. **Autorisez les applications moins sécurisées** (si nécessaire)

### **Pour Office 365 :**
1. **Vérifiez avec votre administrateur IT**
2. **Assurez-vous que l'envoi SMTP est autorisé**
3. **Utilisez le compte de service RH** si disponible

## 📋 **ÉTAPES DE CONFIGURATION**

### **Étape 1 : Choisir le Type**
```bash
python configurer_email_microsoft.py
```

Le script vous demande :
1. **Type d'email** : Outlook.com ou Office 365
2. **Adresse email** : Votre email Microsoft
3. **Mot de passe** : Votre mot de passe

### **Étape 2 : Test Automatique**
Le script teste automatiquement la connexion SMTP.

### **Étape 3 : Utilisation**
```bash
# Interface graphique
interface_graphique.bat

# Ou ligne de commande
python main.py
```

## 🧪 **TEST DE CONFIGURATION**

### **Test Rapide**
```bash
python test_system.py
```

### **Test Manuel**
```python
from email_sender import EmailSender

email_sender = EmailSender()
if email_sender.tester_connexion():
    print("✅ Configuration Microsoft OK !")
else:
    print("❌ Problème de configuration")
```

## ❓ **PROBLÈMES COURANTS**

### **1. "Authentification échouée"**
**Causes possibles :**
- Mot de passe incorrect
- Authentification à 2 facteurs non configurée
- Besoin d'un mot de passe d'application

**Solutions :**
```bash
# Reconfigurez avec le script
python configurer_email_microsoft.py
```

### **2. "Connexion refusée"**
**Causes possibles :**
- Paramètres SMTP incorrects
- Pare-feu bloquant le port 587
- Applications moins sécurisées désactivées

**Solutions :**
- Vérifiez les paramètres SMTP
- Autorisez les applications moins sécurisées
- Contactez votre administrateur réseau

### **3. "SMTP non autorisé" (Office 365)**
**Causes possibles :**
- Politique d'entreprise restrictive
- Compte sans droits d'envoi SMTP
- Configuration Exchange restrictive

**Solutions :**
- Contactez votre administrateur IT
- Demandez l'autorisation d'envoi SMTP
- Utilisez un compte de service dédié

## 🔄 **CHANGEMENT DE FOURNISSEUR**

### **De Gmail vers Microsoft :**
```python
# Dans config.py, changez :
EMAIL_CONFIG = EMAIL_CONFIG_GMAIL      # Ancien
EMAIL_CONFIG = EMAIL_CONFIG_MICROSOFT  # Nouveau
```

### **Entre types Microsoft :**
```python
# Outlook.com vers Office 365 :
EMAIL_CONFIG = EMAIL_CONFIG_MICROSOFT  # Ancien
EMAIL_CONFIG = EMAIL_CONFIG_OFFICE365  # Nouveau
```

## 📊 **COMPARAISON DES FOURNISSEURS**

| Fournisseur | Serveur SMTP | Port | Limite/jour | Facilité |
|-------------|--------------|------|-------------|----------|
| **Gmail** | smtp.gmail.com | 587 | 500 emails | ⭐⭐⭐⭐⭐ |
| **Outlook.com** | smtp-mail.outlook.com | 587 | 300 emails | ⭐⭐⭐⭐ |
| **Office 365** | smtp.office365.com | 587 | Variable | ⭐⭐⭐ |

## 🎯 **RECOMMANDATIONS**

### **Pour 5000+ emails :**
1. **Office 365 Professionnel** (meilleure option)
2. **Gmail avec compte professionnel**
3. **Outlook.com** (pour volumes moyens)

### **Pour usage professionnel :**
- ✅ **Office 365** avec domaine d'entreprise
- ✅ **Compte de service RH** dédié
- ✅ **Authentification renforcée**

## 🚀 **COMMANDES RAPIDES**

```bash
# Configuration Microsoft
python configurer_email_microsoft.py

# Test de la configuration
python test_system.py

# Interface graphique
interface_graphique.bat

# Envoi en mode test
python main.py  # (avec MODE_TEST = True)
```

## 📞 **SUPPORT MICROSOFT**

### **Outlook.com :**
- Support Microsoft : https://support.microsoft.com/outlook
- Paramètres de sécurité : https://account.microsoft.com/security

### **Office 365 :**
- Contactez votre administrateur IT
- Documentation : https://docs.microsoft.com/office365
- Centre d'administration : https://admin.microsoft.com

## 🎉 **RÉSUMÉ**

✅ **Support Microsoft complet** ajouté
✅ **Script de configuration** automatique
✅ **Guide détaillé** avec solutions
✅ **Test automatique** de connexion
✅ **Compatible** avec tous les types Microsoft

**Votre système supporte maintenant Gmail ET Microsoft ! 🚀**

---

## 📝 **EXEMPLE COMPLET**

```bash
# 1. Configuration
python configurer_email_microsoft.py

# 2. Test
python test_system.py

# 3. Utilisation
interface_graphique.bat
```

**Votre email Microsoft est maintenant prêt pour l'envoi en masse ! 📧**
