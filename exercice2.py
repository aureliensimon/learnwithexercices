# Correction de création de classe pour gestion de BDD.

import mysql.connector as mysql

    
class BDD_CLASS:

    # Constructeur.
    def __init__(self, host, database, user, password):

        self.host = host
        self.database = database
        self.user = user
        self.password = password

        self.curseur = None

    def connectBDD(self):
        # Connexion à la base de données.
        self.connexion = mysql.connect( host = self.host, 
                                        database = self.database, 
                                        user = self.user, 
                                        password = self.password,
                                        auth_plugin = 'mysql_native_password') # Pour prévenir de 'caching_sha2_password' 


        # Cursor.
        self.curseur = self.connexion.cursor()
    
    # Close connection.
    def close(self):
        self.curseur.close()
    
    # Exemple de requête.
    def exempleSELECT(self):
        self.connectBDD()

        requete = "SELECT * FROM actor LIMIT 10"

        self.curseur.execute(requete)
        result = self.curseur.fetchall()

        print(result)

        for elt in result:
            print(elt)

        self.close()