from Objects import *

class Plateau:

    def __init__(self, filee):
        with open(filee) as fichier:
            dimensions = fichier.readline().strip()
            mid = dimensions.find(" ")
            self.width = int(dimensions [:mid])
            self.height= int(dimensions[mid+1 :])
            
            self.plate = [[[0] for a in range(self.width)] for i in range(self.height)]
            ajouts = fichier.readlines()
            
            materials = "baba, wall, rock, flag, metal, grass, water, lava"
            #letters = "text_baba, text_wall, text_rock, text_flag, text_water, text_grass, text_lava, stop, push, you, win, best, sink, is"
            
            for i in ajouts:
                description, x, y = i.split()
                x = int(x)
                y = int(y)
                
                if description in materials:
                    self.plate[y][x] = Materials(x, y, description)
                else:
                    self.plate[y][x] = Texts(x, y, description)
    
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
        elif objects.description == "grass":
            m = "🌿 "
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
        elif objects.description == "text_water":
            m = "🇴 "
        elif objects.description == "is":
            m = "✔️ "
        elif objects.description == "stop":
            m = "🇨 "
        elif objects.description == "push":
            m = "🇩 "
        elif objects.description == "you":
            m = "🇯 "
        elif objects.description == "win":
            m = "🇰 "
        elif objects.description == "best":
            m = "🇻 "
        elif objects.description == "sink":
            m = "🇦 "
        
        return m
    
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






























