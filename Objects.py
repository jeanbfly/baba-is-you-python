class Objects:
	# Le constructeur de base de chaque objet
    def __init__(self, x, y, description, direction=0):
        self.x = x
        self.y = y
        self.description = description
        self.dir = direction
    
    def __str__(self):
        d = self.direction_letters()
        
        m = "%s coordonnées: %d %d et direction %s" % (self.description, self.x, self.y, d)
        
        return m

    # Permet de dire explicitement la direction du d'un élément
    def direction_letters(self):
        if self.dir == 0:
            d = "droite"
        elif self.dir == 1:
            d = "haut"
        elif self.dir == 2:
            d = "gauche"
        elif self.dir == 3:
            d = "bas"
        return d

class Materials(Objects):
	# Je pense qu'on peut écrire moins mais je n'ai pas réussi
    def __init__(self, x, y, description, properties=[], direction=0):
        self.x = x
        self.y = y
        self.description = description
        self.properties = properties
        self.dir = direction
    
    def __str__(self):
        d = self.direction_letters()
        
        m = "%s coordonnées: %d %d et direction %s\nProperties: " % (self.description, self.x, self.y, d)
        
        for i in self.properties:
            m += (str(i) + " ")
        return m

    def add_rules(self, rule):
        self.properties.append(rule)

class Texts(Objects):
    pass # Le constructeur Objects est le même

