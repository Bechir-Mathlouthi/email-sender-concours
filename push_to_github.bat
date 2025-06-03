@echo off
echo 🚀 PUSH VERS GITHUB
echo ==================
echo.
echo Ajout du remote GitHub...
git remote add origin https://github.com/Bechir-Mathlouthi/email-sender-concours.git
echo.
echo Push vers GitHub...
git branch -M main
git push -u origin main
echo.
echo ✅ Push terminé !
echo 🌐 Votre projet est maintenant sur : https://github.com/Bechir-Mathlouthi/email-sender-concours
pause
