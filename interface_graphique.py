"""
Interface graphique pour le système d'envoi d'emails personnalisés
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
import pandas as pd
import os
from datetime import datetime
import queue
import time

from pdf_generator import CandidatPDFGenerator
from email_sender import EmailSender
from config import FICHIER_EXCEL, MODE_TEST, NOMBRE_TEST, EMAIL_CONFIG


class InterfaceEnvoiEmails:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("📧 Système d'Envoi d'Emails Personnalisés - Concours")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.df_candidats = None
        self.chemins_pdfs = {}
        self.stats = {'total': 0, 'succes': 0, 'echecs': 0, 'erreurs': []}
        self.envoi_en_cours = False
        self.arreter_demande = False
        self.thread_envoi = None
        self.queue_messages = queue.Queue()
        
        # Créer l'interface
        self.creer_interface()
        
        # Charger les données au démarrage
        self.charger_donnees()
        
        # Démarrer le thread de mise à jour
        self.root.after(100, self.verifier_messages)

        # Gérer la fermeture de l'application
        self.root.protocol("WM_DELETE_WINDOW", self.fermer_application)
    
    def creer_interface(self):
        """Crée l'interface graphique"""
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Titre principal
        titre_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        titre_frame.pack(fill='x', padx=10, pady=5)
        titre_frame.pack_propagate(False)
        
        titre_label = tk.Label(titre_frame, text="📧 Système d'Envoi d'Emails Personnalisés", 
                              font=('Arial', 16, 'bold'), fg='white', bg='#2c3e50')
        titre_label.pack(expand=True)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Section 1: Informations du fichier
        self.creer_section_fichier(main_frame)
        
        # Section 2: Configuration
        self.creer_section_config(main_frame)
        
        # Section 3: Progression
        self.creer_section_progression(main_frame)
        
        # Section 4: Logs
        self.creer_section_logs(main_frame)
        
        # Section 5: Boutons d'action
        self.creer_section_boutons(main_frame)
    
    def creer_section_fichier(self, parent):
        """Section informations du fichier"""
        frame = tk.LabelFrame(parent, text="📊 Informations du Fichier", font=('Arial', 10, 'bold'), 
                             bg='#f0f0f0', fg='#2c3e50')
        frame.pack(fill='x', pady=5)
        
        # Informations
        self.info_frame = tk.Frame(frame, bg='#f0f0f0')
        self.info_frame.pack(fill='x', padx=10, pady=5)
        
        self.label_fichier = tk.Label(self.info_frame, text="Fichier: Non chargé", 
                                     font=('Arial', 9), bg='#f0f0f0')
        self.label_fichier.grid(row=0, column=0, sticky='w', padx=5)
        
        self.label_candidats = tk.Label(self.info_frame, text="Candidats: 0", 
                                       font=('Arial', 9), bg='#f0f0f0')
        self.label_candidats.grid(row=0, column=1, sticky='w', padx=20)
        
        self.label_specialites = tk.Label(self.info_frame, text="Spécialités: 0", 
                                         font=('Arial', 9), bg='#f0f0f0')
        self.label_specialites.grid(row=1, column=0, sticky='w', padx=5)
        
        self.label_score = tk.Label(self.info_frame, text="Score moyen: 0", 
                                   font=('Arial', 9), bg='#f0f0f0')
        self.label_score.grid(row=1, column=1, sticky='w', padx=20)
        
        # Bouton charger fichier
        btn_charger = tk.Button(frame, text="📁 Charger un autre fichier Excel", 
                               command=self.charger_fichier, bg='#3498db', fg='white',
                               font=('Arial', 9, 'bold'))
        btn_charger.pack(pady=5)
    
    def creer_section_config(self, parent):
        """Section configuration"""
        frame = tk.LabelFrame(parent, text="⚙️ Configuration", font=('Arial', 10, 'bold'), 
                             bg='#f0f0f0', fg='#2c3e50')
        frame.pack(fill='x', pady=5)
        
        config_frame = tk.Frame(frame, bg='#f0f0f0')
        config_frame.pack(fill='x', padx=10, pady=5)
        
        # Mode test
        self.var_mode_test = tk.BooleanVar(value=MODE_TEST)
        check_test = tk.Checkbutton(config_frame, text="🧪 Mode Test", 
                                   variable=self.var_mode_test, font=('Arial', 9),
                                   bg='#f0f0f0', command=self.changer_mode)
        check_test.grid(row=0, column=0, sticky='w')
        
        # Nombre de test
        tk.Label(config_frame, text="Nombre d'emails de test:", 
                font=('Arial', 9), bg='#f0f0f0').grid(row=0, column=1, padx=20)
        
        self.var_nombre_test = tk.StringVar(value=str(NOMBRE_TEST))
        spin_test = tk.Spinbox(config_frame, from_=1, to=50, width=5, 
                              textvariable=self.var_nombre_test)
        spin_test.grid(row=0, column=2)
        
        # Email expéditeur
        tk.Label(config_frame, text=f"📧 Email: {EMAIL_CONFIG['expediteur']}", 
                font=('Arial', 9), bg='#f0f0f0').grid(row=1, column=0, columnspan=3, sticky='w', pady=5)
    
    def creer_section_progression(self, parent):
        """Section progression"""
        frame = tk.LabelFrame(parent, text="📈 Progression", font=('Arial', 10, 'bold'), 
                             bg='#f0f0f0', fg='#2c3e50')
        frame.pack(fill='x', pady=5)
        
        prog_frame = tk.Frame(frame, bg='#f0f0f0')
        prog_frame.pack(fill='x', padx=10, pady=5)
        
        # Barre de progression
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(prog_frame, variable=self.progress_var, 
                                           maximum=100, length=400)
        self.progress_bar.pack(fill='x', pady=5)
        
        # Labels de progression
        stats_frame = tk.Frame(prog_frame, bg='#f0f0f0')
        stats_frame.pack(fill='x')
        
        self.label_progression = tk.Label(stats_frame, text="Prêt à commencer", 
                                         font=('Arial', 9, 'bold'), bg='#f0f0f0')
        self.label_progression.grid(row=0, column=0, sticky='w')
        
        self.label_stats = tk.Label(stats_frame, text="Total: 0 | Succès: 0 | Échecs: 0", 
                                   font=('Arial', 9), bg='#f0f0f0', fg='#27ae60')
        self.label_stats.grid(row=1, column=0, sticky='w')
        
        self.label_temps = tk.Label(stats_frame, text="", 
                                   font=('Arial', 9), bg='#f0f0f0', fg='#7f8c8d')
        self.label_temps.grid(row=2, column=0, sticky='w')
    
    def creer_section_logs(self, parent):
        """Section logs"""
        frame = tk.LabelFrame(parent, text="📝 Logs en Temps Réel", font=('Arial', 10, 'bold'), 
                             bg='#f0f0f0', fg='#2c3e50')
        frame.pack(fill='both', expand=True, pady=5)
        
        # Zone de texte avec scrollbar
        self.text_logs = scrolledtext.ScrolledText(frame, height=10, font=('Consolas', 8),
                                                  bg='#2c3e50', fg='#ecf0f1', insertbackground='white')
        self.text_logs.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Ajouter un message de bienvenue
        self.ajouter_log("🎯 Système d'envoi d'emails personnalisés initialisé", "INFO")
    
    def creer_section_boutons(self, parent):
        """Section boutons d'action"""
        frame = tk.Frame(parent, bg='#f0f0f0')
        frame.pack(fill='x', pady=10)
        
        # Bouton tester
        self.btn_tester = tk.Button(frame, text="🧪 Tester la Connexion", 
                                   command=self.tester_connexion, bg='#f39c12', fg='white',
                                   font=('Arial', 10, 'bold'), width=20)
        self.btn_tester.pack(side='left', padx=5)
        
        # Bouton générer PDFs
        self.btn_generer = tk.Button(frame, text="📄 Générer les PDFs", 
                                    command=self.generer_pdfs, bg='#9b59b6', fg='white',
                                    font=('Arial', 10, 'bold'), width=20)
        self.btn_generer.pack(side='left', padx=5)
        
        # Bouton envoyer
        self.btn_envoyer = tk.Button(frame, text="🚀 Envoyer les Emails", 
                                    command=self.envoyer_emails, bg='#27ae60', fg='white',
                                    font=('Arial', 10, 'bold'), width=20)
        self.btn_envoyer.pack(side='left', padx=5)
        
        # Bouton arrêter
        self.btn_arreter = tk.Button(frame, text="⏹️ Arrêter", 
                                    command=self.arreter_envoi, bg='#e74c3c', fg='white',
                                    font=('Arial', 10, 'bold'), width=15, state='disabled')
        self.btn_arreter.pack(side='right', padx=5)
    
    def ajouter_log(self, message, type_msg="INFO"):
        """Ajoute un message aux logs"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Couleurs selon le type
        couleurs = {
            "INFO": "#3498db",
            "SUCCESS": "#27ae60", 
            "ERROR": "#e74c3c",
            "WARNING": "#f39c12"
        }
        
        # Icônes selon le type
        icones = {
            "INFO": "ℹ️",
            "SUCCESS": "✅",
            "ERROR": "❌", 
            "WARNING": "⚠️"
        }
        
        log_message = f"[{timestamp}] {icones.get(type_msg, 'ℹ️')} {message}\n"
        
        # Ajouter au queue pour thread safety
        self.queue_messages.put(('log', log_message, couleurs.get(type_msg, "#ecf0f1")))
    
    def verifier_messages(self):
        """Vérifie les messages dans la queue"""
        try:
            while True:
                type_msg, message, couleur = self.queue_messages.get_nowait()
                if type_msg == 'log':
                    self.text_logs.insert(tk.END, message)
                    self.text_logs.see(tk.END)
                elif type_msg == 'progress':
                    self.progress_var.set(message)
                elif type_msg == 'stats':
                    self.label_stats.config(text=message)
                elif type_msg == 'status':
                    self.label_progression.config(text=message)
        except queue.Empty:
            pass
        
        # Programmer la prochaine vérification
        self.root.after(100, self.verifier_messages)
    
    def charger_donnees(self):
        """Charge les données du fichier Excel"""
        try:
            if os.path.exists(FICHIER_EXCEL):
                self.df_candidats = pd.read_excel(FICHIER_EXCEL)
                self.mettre_a_jour_infos_fichier()
                self.ajouter_log(f"Fichier {FICHIER_EXCEL} chargé avec succès", "SUCCESS")
            else:
                self.ajouter_log(f"Fichier {FICHIER_EXCEL} non trouvé", "ERROR")
        except Exception as e:
            self.ajouter_log(f"Erreur lors du chargement: {e}", "ERROR")
    
    def mettre_a_jour_infos_fichier(self):
        """Met à jour les informations du fichier"""
        if self.df_candidats is not None:
            nb_candidats = len(self.df_candidats)
            nb_specialites = self.df_candidats['Spécialité'].nunique() if 'Spécialité' in self.df_candidats.columns else 0
            score_moyen = self.df_candidats['Score'].mean() if 'Score' in self.df_candidats.columns else 0
            
            self.label_fichier.config(text=f"Fichier: {FICHIER_EXCEL}")
            self.label_candidats.config(text=f"Candidats: {nb_candidats}")
            self.label_specialites.config(text=f"Spécialités: {nb_specialites}")
            self.label_score.config(text=f"Score moyen: {score_moyen:.1f}")
    
    def charger_fichier(self):
        """Charge un nouveau fichier Excel"""
        fichier = filedialog.askopenfilename(
            title="Sélectionner le fichier Excel des candidats",
            filetypes=[("Fichiers Excel", "*.xlsx *.xls")]
        )
        
        if fichier:
            try:
                self.df_candidats = pd.read_excel(fichier)
                self.mettre_a_jour_infos_fichier()
                self.ajouter_log(f"Nouveau fichier chargé: {os.path.basename(fichier)}", "SUCCESS")
            except Exception as e:
                self.ajouter_log(f"Erreur lors du chargement: {e}", "ERROR")
                messagebox.showerror("Erreur", f"Impossible de charger le fichier:\n{e}")
    
    def changer_mode(self):
        """Change le mode test/production"""
        if self.var_mode_test.get():
            self.ajouter_log("Mode TEST activé", "WARNING")
        else:
            self.ajouter_log("Mode PRODUCTION activé", "WARNING")
    
    def tester_connexion(self):
        """Teste la connexion email"""
        def test():
            try:
                self.ajouter_log("Test de connexion SMTP en cours...", "INFO")
                email_sender = EmailSender()
                if email_sender.tester_connexion():
                    self.ajouter_log("Connexion SMTP réussie !", "SUCCESS")
                    messagebox.showinfo("Succès", "Connexion email testée avec succès !")
                else:
                    self.ajouter_log("Échec de la connexion SMTP", "ERROR")
                    messagebox.showerror("Erreur", "Échec de la connexion email")
            except Exception as e:
                self.ajouter_log(f"Erreur de test: {e}", "ERROR")
                messagebox.showerror("Erreur", f"Erreur lors du test:\n{e}")
        
        threading.Thread(target=test, daemon=True).start()
    
    def generer_pdfs(self):
        """Génère les PDFs"""
        if self.df_candidats is None:
            messagebox.showerror("Erreur", "Aucun fichier de candidats chargé")
            return
        
        def generer():
            try:
                self.ajouter_log("Génération des PDFs en cours...", "INFO")
                self.queue_messages.put(('status', "Génération des PDFs...", None))
                
                pdf_generator = CandidatPDFGenerator()
                self.chemins_pdfs = pdf_generator.generer_tous_les_pdfs(self.df_candidats)
                
                pdfs_generes = len([p for p in self.chemins_pdfs.values() if p])
                self.ajouter_log(f"{pdfs_generes} PDFs générés avec succès", "SUCCESS")
                self.queue_messages.put(('status', f"{pdfs_generes} PDFs générés", None))
                
                messagebox.showinfo("Succès", f"{pdfs_generes} PDFs générés avec succès !")
                
            except Exception as e:
                self.ajouter_log(f"Erreur génération PDFs: {e}", "ERROR")
                messagebox.showerror("Erreur", f"Erreur lors de la génération:\n{e}")
        
        threading.Thread(target=generer, daemon=True).start()
    
    def envoyer_emails(self):
        """Envoie les emails"""
        if self.df_candidats is None:
            messagebox.showerror("Erreur", "Aucun fichier de candidats chargé")
            return

        if not self.chemins_pdfs:
            if messagebox.askyesno("PDFs manquants", "Aucun PDF généré. Voulez-vous les générer maintenant ?"):
                self.generer_pdfs()
                return
            else:
                return

        # Confirmation
        mode = "TEST" if self.var_mode_test.get() else "PRODUCTION"
        nb_emails = int(self.var_nombre_test.get()) if self.var_mode_test.get() else len(self.df_candidats)

        if not messagebox.askyesno("Confirmation",
                                  f"Envoyer {nb_emails} emails en mode {mode} ?\n\n"
                                  f"Cette action ne peut pas être annulée."):
            return

        # Réinitialiser les variables d'arrêt
        self.arreter_demande = False
        self.envoi_en_cours = True
        self.btn_envoyer.config(state='disabled')
        self.btn_arreter.config(state='normal')

        def envoyer():
            try:
                self.ajouter_log(f"Début de l'envoi en mode {mode}", "INFO")
                self.queue_messages.put(('status', f"Envoi en cours ({mode})...", None))

                email_sender = EmailSender()

                # Préparer les données
                df_envoi = self.df_candidats.copy()
                if self.var_mode_test.get():
                    df_envoi = df_envoi.head(int(self.var_nombre_test.get()))

                # Envoi avec suivi de progression
                self.envoyer_avec_progression(email_sender, df_envoi)

            except Exception as e:
                self.ajouter_log(f"Erreur envoi: {e}", "ERROR")
                messagebox.showerror("Erreur", f"Erreur lors de l'envoi:\n{e}")
            finally:
                self.envoi_en_cours = False
                self.arreter_demande = False
                self.btn_envoyer.config(state='normal')
                self.btn_arreter.config(state='disabled')

        # Stocker la référence du thread
        self.thread_envoi = threading.Thread(target=envoyer, daemon=True)
        self.thread_envoi.start()
    
    def envoyer_avec_progression(self, email_sender, df_envoi):
        """Envoie les emails avec suivi de progression"""
        if not email_sender.connecter_serveur():
            self.ajouter_log("Impossible de se connecter au serveur SMTP", "ERROR")
            return

        total = len(df_envoi)
        succes = 0
        echecs = 0

        self.stats = {'total': total, 'succes': 0, 'echecs': 0, 'erreurs': []}

        for index, (idx, row) in enumerate(df_envoi.iterrows()):
            # Vérifier si l'arrêt a été demandé
            if self.arreter_demande or not self.envoi_en_cours:
                self.ajouter_log("⏹️ Envoi arrêté par l'utilisateur", "WARNING")
                break

            candidat_data = row.to_dict()
            chemin_pdf = self.chemins_pdfs.get(idx)

            # Mettre à jour la progression
            progression = (index / total) * 100
            self.queue_messages.put(('progress', progression, None))

            # Envoyer l'email
            nom = candidat_data.get('Nom', 'N/A')
            email = candidat_data.get('Email', 'N/A')

            if not chemin_pdf:
                self.ajouter_log(f"PDF manquant pour {nom}", "WARNING")
                echecs += 1
                continue

            if not email or email == 'N/A':
                self.ajouter_log(f"Email manquant pour {nom}", "WARNING")
                echecs += 1
                continue

            # Vérifier à nouveau avant l'envoi
            if self.arreter_demande:
                self.ajouter_log("⏹️ Envoi arrêté avant l'email suivant", "WARNING")
                break

            try:
                if email_sender.envoyer_email(candidat_data, chemin_pdf):
                    succes += 1
                    self.ajouter_log(f"Email envoyé à {nom} ({email})", "SUCCESS")
                else:
                    echecs += 1
                    self.ajouter_log(f"Échec envoi pour {nom}", "ERROR")
            except Exception as e:
                echecs += 1
                self.ajouter_log(f"Erreur pour {nom}: {e}", "ERROR")

            # Mettre à jour les statistiques
            stats_text = f"Total: {total} | Succès: {succes} | Échecs: {echecs}"
            self.queue_messages.put(('stats', stats_text, None))

            # Petit délai pour éviter la surcharge et permettre l'arrêt
            for i in range(5):  # 5 vérifications de 0.1s = 0.5s total
                if self.arreter_demande:
                    break
                time.sleep(0.1)

        email_sender.deconnecter_serveur()

        # Progression finale
        if not self.arreter_demande:
            self.queue_messages.put(('progress', 100, None))
            self.queue_messages.put(('status', f"Terminé: {succes} succès, {echecs} échecs", None))
        else:
            self.queue_messages.put(('status', f"Arrêté: {succes} succès, {echecs} échecs", None))

        # Message final
        if self.arreter_demande:
            self.ajouter_log(f"⏹️ Envoi arrêté ! {succes} emails envoyés avant l'arrêt", "WARNING")
        elif succes > 0:
            self.ajouter_log(f"🎉 Envoi terminé ! {succes} emails envoyés avec succès", "SUCCESS")

        if echecs > 0:
            self.ajouter_log(f"⚠️ {echecs} emails n'ont pas pu être envoyés", "WARNING")
    
    def arreter_envoi(self):
        """Arrête l'envoi en cours"""
        if messagebox.askyesno("Confirmation", "Voulez-vous vraiment arrêter l'envoi en cours ?"):
            self.arreter_demande = True
            self.envoi_en_cours = False
            self.ajouter_log("🛑 Demande d'arrêt envoyée...", "WARNING")
            self.queue_messages.put(('status', "Arrêt en cours...", None))

            # Désactiver le bouton arrêter pour éviter les clics multiples
            self.btn_arreter.config(state='disabled', text="⏳ Arrêt...")

            # Réactiver le bouton envoyer après un délai
            def reactiver_boutons():
                time.sleep(2)  # Attendre 2 secondes
                self.btn_envoyer.config(state='normal')
                self.btn_arreter.config(state='disabled', text="⏹️ Arrêter")

            threading.Thread(target=reactiver_boutons, daemon=True).start()

    def fermer_application(self):
        """Ferme l'application proprement"""
        if self.envoi_en_cours:
            if messagebox.askyesno("Envoi en cours",
                                  "Un envoi d'emails est en cours.\n\n"
                                  "Voulez-vous vraiment fermer l'application ?\n"
                                  "L'envoi sera arrêté."):
                self.arreter_demande = True
                self.envoi_en_cours = False
                self.ajouter_log("🚪 Fermeture de l'application...", "INFO")
                self.root.destroy()
        else:
            self.root.destroy()

    def run(self):
        """Lance l'interface"""
        self.root.mainloop()


if __name__ == "__main__":
    app = InterfaceEnvoiEmails()
    app.run()
