class Animal:
    def sayAnimal(self):
        return "I am an animal"

class AnimalFriend:
    def sayFriend(self):
        return "My friend is Mr. Farmer"


class Cow(Animal, AnimalFriend):
    def sayCowThing(self):
        print(f"{self.sayAnimal()} and {self.sayFriend()}")

# class Lion(Animal):

bossie = Cow()
bossie.sayCowThing()

# ========================

class Bird:
    def __init__(self, species, nest="tree"):
        self.has_feathers = True
        self.species = species
        self.nest = nest

    def layEgg(self):
        if self.nest == "tree":
            return ("Im a bird")
        else:
            return("Push!")
    
class Flying:
    def __init__(self):
        self.can_fly = True

    @property
    def wings(self):
        try:
            return self._wing_count
        except AttributeError:
            return 2

    @wings.setter
    def wings(self, count):
        if isinstance(count, int):
            self.__wing_count = count 
        else: 
            raise TypeError("Wing count must be a number")

    def fly(self):
        print("I want to fly like an eagle, to the sea.")

class Swimming:
    def __init__(self):
        self.can_swim = True

    def swim(self): 
        print("I want to swim like a penquin, in the sea.")

class Running:
    def __init__(self, leg_length):
        self.can_run = True
        self.run_speed = 2.0 
        self.leg_length = leg_length


    def run(self):
        if self.leg_length < 10 and self.run_speed <= 2.0:
            return "I'm waddling as fast as I can."
        elif self.leg_length < 20:
            return "I'm running now, but get closer and I'll fly instead"
        else:
            return "Catch me if you can."
class Bat(Flying):
    def __init__(self,species): 
        self.has_feathers = False
        self.species = species

class Penguin(Bird, Running, Swimming):

    def __init__(self, species, nest="ground", leg_length=5):
        self.color = "black and white"


        Bird.__init__(self, species, nest)
        Swimming.__init__(self)
        Running.__init__(self, leg_length)

        def __str__(self):
            return f'can_run: {self.can_run}, can_swim: {self.can_swim}, has_feathers: {self.has_feathers}'


emperor_penguin = Penguin("Emperor Penguin")
print("Our running, swimming, feathery penguin", emperor_penguin)


class Developer:
    def __init__(self, education):
        self.is_human = True
        self.BO = True
        self.education = education

    def introverted(self):
        if self.BO == True:
            return ("I code for days without showering")
        else:
            return("Im a 'new age' coder")

class Coding: 
    def __init__(self):
        self.can_code = True

    @property
    def languages(self):
        try:
            return self._language_count
        except AttributeError:
            return 2

    @languages.setter
    def languages(self, count):
        if isinstance(count, int):
            self._language_count = count
        else: 
            raise TypeError("Language count must be a number")

    def code(self):
        print("I code beeetch")

class JohnWood(Developer, Coding):

    def __init__(self, education, is_human = True, BO = True):
        self.ethnicity = "Asian"

        Developer.__init__(self, education)

    def __str__(self):
        return f'can_code: {self.can_code}'

JohnWood = Developer("NSS")
print("Test", JohnWood) 



        



            



    
   
    

