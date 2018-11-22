import random
from virus import * 
from simulation import *

class Person(object):

    def __init__(self, _id, is_vaccinated=bool, infected=None):
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # to set the corret values for the following attributes.
        self._id = _id
        self.is_vaccinated = is_vaccinated #This can vary 
        self.is_alive = True
        self.infected = infected #Virus()
        # if person chosen to be infected first, object should create a Virus object with value for self.infected
        # for some reason this print is = None for every person
        # print(self.is_vaccinated)

        # if self.infected is None and self.is_vaccinated is False:
        #     did_survive_infection()
    # Check if the person survived the infection.
    def did_survive_infection(self, mortality_rate):
        # print("running did_surv")
        if self.infected is not None:
            if random.random() <= mortality_rate:
                self.is_alive = False
                self.infected = None
                return False
            else:
                # Maf'k survived
                # print("Maf'k survived")
                self.is_vaccinated = True
                self.infected = None
                return True
