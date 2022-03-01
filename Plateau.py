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
            
            # Liste pour différiencer les matériaux et les textes
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
                    self.plate[y][x].append(Materials(x, y, description))
                else:
                    self.plate[y][x].append(Texts(x, y, description))
    
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
        for x in range(len(self.plate)):
            for y in range(len(self.plate[0])):
                if not self.plate[x][y] == [] and isinstance(self.plate[x][y][0], Objects):
                    res += self.image(self.plate[x][y][0])
                else:
                    res += "0️ "
            res += '\n'
        return res
    
    def findRules(self):
        """
        On parcourt toutes la matrice
        On vérifie si on trouve un objet
        On vérifie si on trouve un "is"
        On regarde sur l'axe des x puis des y
        Sur chaque axes regarder si on a un text_matériaux à gauche et/ou en haut et un text_properties à droite et/ou en bas
        Créer une chaine avec les trois éléments si ils sont alignés
        Ajouter la chaine à la liste des règles
        """
        
        rules = []
        for x in range(len(self.plate)):
            for y in range(len(self.plate[0])):
                if len(self.plate[x][y]) > 0 and self.plate[x][y][0].description == "is":
                    if 0 < x < len(self.plate)-2:
                        if len(self.plate[x-1][y]) > 0 and len(self.plate[x+1][y]) > 0 and self.plate[x-1][y][0].description in self.text_materials and self.plate[x+1][y][0].description in self.text_properties:
                            rules.append(self.plate[x-1][y][0].description + " is " +  self.plate[x+1][y][0].description)
                    if 0 < y < len(self.plate[0])-2:
                        if len(self.plate[x][y-1]) > 0 and len(self.plate[x][y+1]) > 0 and self.plate[x][y-1][0].description in self.text_materials and self.plate[x][y+1][0].description in self.text_properties:
                            rules.append(self.plate[x][y-1][0].description + " is " +  self.plate[x][y+1][0].description)
        print(rules)
    
    """
    fonction permettant d'ajouter à chaque objet 
    du même type la même propriété
    """
    # A améliorer
    def add_all(obj, prop):
        for x in range(len(self.plate)):
            for y in range(len(self.plate[0])):
                if len(self.plate[x][y]) > 0 and self.plate[x][y][0].description == obj.description:
                    self.plate[x][y][0].add_rules(prop)
    
    """ 
    fonction permettant de bouger tous les 
    objets comportant l'argument you
    """
    def can_move(self, focus, x, y):
        # on inverse les coordonnées quand on passe de la vrai position à la matrice
        i = focus.getY() +x
        j = focus.getX() +y
        
        if 0 < i < len(self.plate) and 0 < j < len(self.plate[i]):
            for k in self.plate[i][j]:
                if isinstance(k, Texts) or isinstance(k, Materials) and "push" in k.properties:
                    return self.can_move(k, x, y)
            return True
        else:
            return False
    
    def findYou(self):
        pass
    """
    def move(self, direction):
        x = 0
        y = 0
        
        if direction == "right":
            y = 1
        elif direction == "up":
            x = -1
        elif direction == "left":
            y = -1
        elif direction == "down":
            x = 1
        
        # à améliorer car il peut y avoir deux matériaux pour un focus
        # renvoie un type de matériau, (une chaine de caractère)
        focus = self.findYou():
        
        for i in self.plate:
            for j in i:
                for k in j:
                    if isinstance(k, Materials) and focus in k.description:
                        if self.can_move(k, x, y):
                            k.setPosition(x, y)
    """
    def is_win(self):
        """
        méthode qui regarde à chaque case s'il y a un matériel avec la propriété "you"
        et un matériel avec la propriété "win"
        ( Ca peut être le même matériel )
        """
        
        win = False
        you = False
        for x in range(len(self.plate)):
            for y in range(len(self.plate[x])):
                for i in self.plate[x][y]:
                    if isinstance(i, Materials):
                        if "you" in i.properties:
                            you = True
                        if "win" in i.properties:
                            win = True
                    if you and win:
                        return win
                    else:
                        you = False
                        win = False
        return False

