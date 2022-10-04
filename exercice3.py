from flask import Flask, render_template, request
import mysql.connector as mysql

# from animal import Animal

class BDD:

    # Constructeur.
    def __init__(self, host, database, user, password, port):

        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port


    def connectBDD(self):
        # Connexion à la base de données.
        self.connexion = mysql.connect( host = self.host, 
                                        database = self.database, 
                                        user = self.user, 
                                        password = self. password,
                                        port = self.port,
                                        auth_plugin = 'mysql_native_password') # Pour prévenir de 'caching_sha2_password' 


        # Cursor.
        self.cursor = self.connexion.cursor()

    # Close connection.
    def close(self):
        self.cursor.close()
    

    # Récupère tous les animaux
    def dbSelectAllAnimaux(self):
        self.connectBDD()
        
        req = "SELECT id, nom FROM animal"

        self.cursor.execute(req)

        result = self.cursor.fetchall()

        self.close()

        return result

    # Récupère tous les animaux
    def dbSelectAllInfoFromAnimaux(self):
        self.connectBDD()
        
        req = "SELECT * FROM animal"

        self.cursor.execute(req)

        result = self.cursor.fetchall()

        self.close()

        return result

    def dbSelectInfo(self, id_animal):
        self.connectBDD()
        
        req = "SELECT nom, taxome, description, photo from animal WHERE id = %s"
        param = (id_animal, )


        self.cursor.execute(req, param)
        

        result = self.cursor.fetchone()

        self.close()

        return result
    
    def dbSelectLieux(self, id_animal):
        self.connectBDD()
        
        req = "SELECT h.lieu_habitat \
               FROM animal a \
               JOIN animal_habitat ah ON a.id = ah.id \
               JOIN habitat h ON h.id_habitat = ah.id_habitat\
               WHERE a.id = %s"
            
        param = (id_animal, )


        self.cursor.execute(req, param)
        

        result = self.cursor.fetchall()

        self.close()

        return result

class Animal:
    def __init__(self, id, nom, taxome, description, photo, habitat):
        self.id = id
        self.nom = nom
        self.taxome = taxome
        self.description = description
        self.photo = photo
        self.habitat = habitat

class Zoo:
    def __init__(self):
        self.list_animaux = {}

    def addAnimal(self, animal):
        self.list_animaux[animal.id] = animal

    def getAnimal(self, index):
        return self.list_animaux[index]

    def population(self, bdd):
        population = bdd.dbSelectAllInfoFromAnimaux()
        for ids, nom, taxome, description, photo in population:

            habitat = [q[0] for q in bdd.dbSelectLieux(ids)]
            
            animal = Animal(ids, nom, taxome, description, photo, habitat)
            self.addAnimal(animal)
    
    def getAllIdAndNom(self):
        animaux = []
        for animal in self.list_animaux:
            animaux.append((self.list_animaux[animal].id, self.list_animaux[animal].nom))
        return animaux


app = Flask(__name__)

bdd = BDD(host="localhost", database="zoo_tutorat", user="younes", password="yhqdnozEDR176$*&d", port=3306)
zoo = Zoo()
zoo.population(bdd)


@app.route('/')
def index():

    list_animaux = zoo.getAllIdAndNom()

    return render_template('index.html', zoo = list_animaux)

@app.route('/animal', methods = ['POST', 'GET'])
def show_animal():
    if request.method == 'POST':
        id_animal = request.form.get('list_animaux')
    
    info = zoo.getAnimal(int(id_animal))
    return render_template('animal.html', animal=info)