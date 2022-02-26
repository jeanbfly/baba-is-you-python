from Objects import *

class Plateau:

    def __init__(self, filee):
        # Lire le fichier niveau
        with open(filee) as fichier:
            dimensions = fichier.readline().strip()
            mid = dimensions.find(" ")
            self.width = int(dimensions [:mid])
            self.height= int(dimensions[mid+1 :])
            
            self.plate = [[[] for a in range(self.width)] for i in range(self.height)]
            ajouts = fichier.readlines()
            
            # Liste pour différiencer les matériaux est les textes
            self.materials = "baba, wall, rock, flag, metal, grass, goop, lava"
            self.text_materials = "text_baba, text_wall, text_rock, text_flag, text_goop, text_grass, text_lava, text_best"
            self.text_properties = "stop, push, you, win, best, sink, kill"
            
            # Remplir la matrice avec les références de chaque objet
            for i in ajouts:
                description, x, y = i.split()
                x = int(x)
                y = int(y)
                
                # Attention: on inverse x et y dans la matrice
                if description in self.materials:
                    self.plate[y][x] = Materials(x, y, description)
                else:
                    self.plate[y][x] = Texts(x, y, description)
    
    # Renvoie un emojis en fonction de la description d'un objet
    def image(self, objects):
        if objects.description == "baba":
            m = "😀"
        elif objects.description == "flag":
            m = "🏁"
        elif objects.description == "wall":
            m = "🧱"
        elif objects.description == "rock":
            m = "🪨 "
        elif objects.description == "metal": # c'est comme si il n'y avait rien
            m = "0️ "
        elif objects.description == "goop":
            m = "🌊"
        elif objects.description == "grass":
            m = "🌿"
        elif objects.description == "lava":
            m = "🌋"
        
        elif objects.description == "text_baba":
            m = "🇧 "
        elif objects.description == "text_flag":
            m = "🇫 "
        elif objects.description == "text_wall":
            m = "🇼 "
        elif objects.description == "text_rock":
            m = "🇷 "
        elif objects.description == "text_grass":
            m = "🇬 "
        elif objects.description == "text_goop":
            m = "🇴 "
        elif objects.description == "text_lava":
            m = "🇱 "
        
        elif objects.description == "is":
            m = "✔️ "
        elif objects.description == "stop":
            m = "⛔"#🛑
        elif objects.description == "push":
            m = "💪"
        elif objects.description == "you":
            m = "👇"
        elif objects.description == "win":
            m = "🎆"
        elif objects.description == "best":
            m = "✨"
        elif objects.description == "sink":
            m = "🚰"
        elif objects.description == "kill":
            m = "☠️ "
        
        return m
    
    # Affiche la matrice
    def __str__(self):
        res = "\n"
        for x in self.plate:
            for y in x:
                if isinstance(y, Objects):
                    res += self.image(y)
                else:
                    res += "0️ "
            res += '\n'
        return res
    
    def findRules(self):
        rules = []
        """
        On parcourt toutes la matrice
        On vérifie si on trouve un objet
        On vérifie si on trouve un "is"
        On regarde sur l'axe des x puis des y
        Sur chaque axes regarder si on a un text_matériaux à gauche et/ou en haut et un text_properties à droite et/ou en bas
        Créer une chaine avec les trois éléments si ils sont alignés
        Ajouter la chaine à la liste des règles
        """
        for x in range(len(self.plate)):
            for y in range(len(self.plate[x])):
                if isinstance(self.plate[x][y], Objects):
                    if self.plate[x][y].description == "is":
                        if 0 < x < len(self.plate)-2:
                            if isinstance(self.plate[x-1][y], Texts):
                                if self.plate[x-1][y].description in self.text_materials:
                                    if isinstance(self.plate[x+1][y], Texts):
                                        if self.plate[x+1][y].description in self.text_properties:
                                            text = self.plate[x-1][y].description + " is " +  self.plate[x+1][y].description
                                            rules.append(text)
                        if 0 < y < len(self.plate[x])-2:
                            if isinstance(self.plate[x][y-1], Texts):
                                if self.plate[x][y-1].description in self.text_materials:
                                    if isinstance(self.plate[x][y+1], Texts):
                                        if self.plate[x][y+1].description in self.text_properties:
                                            text = self.plate[x][y-1].description + " is " +  self.plate[x][y+1].description
                                            rules.append(text)
        print(rules)




























