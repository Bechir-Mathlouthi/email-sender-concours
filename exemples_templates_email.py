"""
Exemples de templates d'emails pour différents contextes
Copiez-collez le template souhaité dans config.py
"""

# Template actuel (par défaut)
TEMPLATE_ACTUEL = {
    'sujet': 'Résultats de votre candidature - Concours',
    'corps': """Bonjour {nom},

Félicitations ! Vous avez été sélectionné(e) pour la prochaine étape du concours.

Veuillez trouver ci-joint votre fiche de candidature avec vos informations détaillées.

Nous vous contacterons prochainement pour les étapes suivantes.

Cordialement,
Le Service des Ressources Humaines"""
}

# Template professionnel formel
TEMPLATE_PROFESSIONNEL = {
    'sujet': 'Admission - Concours de Recrutement 2025',
    'corps': """Madame, Monsieur {nom},

Nous avons l'honneur de vous informer que votre candidature a été retenue suite à l'examen de votre dossier de candidature au concours de recrutement.

Vous trouverez en pièce jointe votre fiche de candidature détaillée contenant l'ensemble de vos informations.

Nous vous contacterons prochainement pour vous communiquer les modalités et le calendrier de la suite du processus de sélection.

Nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.

Le Service des Ressources Humaines
Direction Générale"""
}

# Template moderne et convivial
TEMPLATE_MODERNE = {
    'sujet': '🎉 Félicitations {nom} - Vous êtes sélectionné(e) !',
    'corps': """Bonjour {nom},

🎊 Excellente nouvelle ! Votre candidature a été retenue !

📄 Votre dossier complet est en pièce jointe
📞 Nous vous appellerons sous 48h
✨ Préparez-vous pour la suite de l'aventure !

Des questions ? Répondez à cet email !

À très bientôt,
L'équipe RH 🚀"""
}

# Template avec instructions détaillées
TEMPLATE_AVEC_INSTRUCTIONS = {
    'sujet': 'Admission confirmée - Prochaines étapes à suivre',
    'corps': """Cher(e) {nom},

Félicitations ! Vous êtes admis(e) à la prochaine phase du concours.

📋 PROCHAINES ÉTAPES :
1. Consultez attentivement votre fiche en pièce jointe
2. Préparez les documents originaux mentionnés
3. Attendez notre convocation par email ou téléphone
4. Restez disponible pour les 2 prochaines semaines

📧 Contact : recrutement@entreprise.com
📞 Téléphone : +216 XX XXX XXX
🕒 Horaires : 8h-17h, Lundi-Vendredi

Félicitations encore et à bientôt !
L'équipe de Recrutement"""
}

# Template pour convocation
TEMPLATE_CONVOCATION = {
    'sujet': 'Convocation - Entretien de sélection',
    'corps': """Bonjour {nom},

Suite à votre sélection, vous êtes convoqué(e) pour un entretien.

📅 DÉTAILS DE LA CONVOCATION :
• Date : À confirmer par téléphone
• Lieu : Siège social - Tunis
• Durée : Environ 45 minutes
• Documents à apporter : CIN + Diplômes originaux

📄 Votre dossier de candidature est en pièce jointe pour révision.

⚠️ IMPORTANT : Confirmez votre présence par retour d'email.

Cordialement,
Service de Recrutement"""
}

# Template pour résultats avec score
TEMPLATE_AVEC_SCORE = {
    'sujet': 'Résultats du concours - Score obtenu',
    'corps': """Bonjour {nom},

Nous avons le plaisir de vous communiquer vos résultats au concours.

🎯 VOTRE SCORE : {score}/100
✅ STATUT : ADMIS(E)
📊 Vous faites partie des candidats sélectionnés !

Votre fiche détaillée est en pièce jointe.

Prochaine étape : Entretien individuel
Nous vous contacterons dans les 5 jours ouvrables.

Félicitations !
Le Jury du Concours"""
}

# Template pour admission définitive
TEMPLATE_ADMISSION_DEFINITIVE = {
    'sujet': 'ADMISSION DÉFINITIVE - Bienvenue dans notre équipe !',
    'corps': """Cher(e) {nom},

🎉 FÉLICITATIONS ! Votre admission est définitive !

Nous sommes ravis de vous accueillir dans notre équipe.

📋 PROCHAINES ÉTAPES :
• Signature du contrat : Semaine prochaine
• Intégration : Date à convenir
• Formation : Programme personnalisé

📄 Votre dossier final est en pièce jointe.

Bienvenue parmi nous !
La Direction des Ressources Humaines"""
}

# Template pour liste d'attente
TEMPLATE_LISTE_ATTENTE = {
    'sujet': 'Candidature retenue - Liste d\'attente',
    'corps': """Bonjour {nom},

Votre candidature a été évaluée positivement.

📋 SITUATION ACTUELLE :
Vous êtes actuellement sur notre liste d'attente prioritaire.

📞 PROCHAINES ÉTAPES :
Nous vous contacterons dès qu'une place se libère.
Restez disponible pour les 4 prochaines semaines.

📄 Votre dossier est en pièce jointe pour vos archives.

Merci pour votre patience.
Service de Recrutement"""
}

# Template multilingue (Français/Arabe)
TEMPLATE_BILINGUE = {
    'sujet': 'نتائج المسابقة - Résultats du concours',
    'corps': """Bonjour {nom} / مرحبا

Félicitations ! Vous avez été sélectionné(e).
!تهانينا! لقد تم اختياركم

Votre dossier est en pièce jointe.
ملفكم مرفق بهذه الرسالة

Cordialement / مع أطيب التحيات
Service RH / مصلحة الموارد البشرية"""
}

# Instructions pour utiliser ces templates
INSTRUCTIONS = """
COMMENT UTILISER CES TEMPLATES :

1. Choisissez le template qui vous convient
2. Ouvrez le fichier config.py
3. Remplacez la section EMAIL_TEMPLATE par le template choisi
4. Sauvegardez le fichier
5. Testez avec MODE_TEST = True

EXEMPLE :
Copiez le contenu de TEMPLATE_MODERNE et remplacez dans config.py :

EMAIL_TEMPLATE = {
    'sujet': '🎉 Félicitations {nom} - Vous êtes sélectionné(e) !',
    'corps': '''Bonjour {nom},
    
    🎊 Excellente nouvelle ! Votre candidature a été retenue !
    ...'''
}
"""

if __name__ == "__main__":
    print("📧 EXEMPLES DE TEMPLATES D'EMAILS")
    print("=" * 50)
    print("\nTemplates disponibles :")
    print("1. TEMPLATE_ACTUEL - Template par défaut")
    print("2. TEMPLATE_PROFESSIONNEL - Formel et officiel")
    print("3. TEMPLATE_MODERNE - Avec emojis et style moderne")
    print("4. TEMPLATE_AVEC_INSTRUCTIONS - Avec étapes détaillées")
    print("5. TEMPLATE_CONVOCATION - Pour convocation entretien")
    print("6. TEMPLATE_AVEC_SCORE - Inclut le score du candidat")
    print("7. TEMPLATE_ADMISSION_DEFINITIVE - Pour admission finale")
    print("8. TEMPLATE_LISTE_ATTENTE - Pour liste d'attente")
    print("9. TEMPLATE_BILINGUE - Français/Arabe")
    print("\n📝 Consultez le fichier pour voir le contenu complet de chaque template.")
    print("📋 Copiez-collez le template souhaité dans config.py")
