import random, sys

random.seed(42)

from person import *
from logger import *
from virus import *

class Simulation(object):

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        # print("running init")
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.initial_infected = initial_infected
        # self.virus_obj = 
        self.total_infected = initial_infected
        self.current_infected = initial_infected
        self.next_person_id = 0

        # keep track of how many people are dead
        self.total_dead = 0

        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)

        self.logger = Logger(self.file_name)

        self.newly_infected = []

        self.population = self._create_population(self.initial_infected)
        print("Population Size:", self.population_size)
        # for person in self.population:
        #     print('Person#', person._id, 'Alive:', person.is_alive, 'Infected:', (person.infected is not None), 'Vaccinated:', person.is_vaccinated)
    def _create_population(self, initial_infected):

        self.logger.write_metadata(self.population_size, self.vacc_percentage, self.virus_name,
                                   self.mortality_rate, self.basic_repro_num)
        
        population = []
        infected_count = 0
        # slightly tricked by this line.
        # so pop_size is being grabbed fro the Simulations parameters when we call it.
        for userId in range(self.population_size):
            # print(len(population))
            # TODO: Create all the infected people first, and then worry about the rest.
            # Don't forget to increment infected_count every time you create a
            # new infected person!
            # print(infected_count, initial_infected)
            if infected_count <= initial_infected:
                # pass in: _id, is_vaccinated, infected=None
                # Haven't create Virus obj yet.
                # create a Person with no vacc 
                # print('This is the virus objects mortality rate %s' %(self.virus_obj.mortality_rate))
                virus_obj = Virus(self.virus_name, self.mortality_rate, self.basic_repro_num)
                new_person_infected = Person(userId, False, virus_obj)
                # instances of the object: we're giving everyone a copy... each person is their own person class, their own attributes.
                # Virus(self.virus_name, self.mortality_rate, self.basic_repro_num)
                population.append(new_person_infected)
                infected_count+=1
            else:
                # Now create all the rest of the people.
                # Every time a new person will be created, generate a random number between
                # 0 and 1.  If this number is smaller than vacc_percentage, this person
                # should be created as a vaccinated person. If not, the person should be
                # created as an unvaccinated person.
                if random.random() < self.vacc_percentage:
                    # safe person
                    vacc_person = Person(userId, True, None)
                    population.append(vacc_person)
                else:
                    unvacc_person = Person(userId, False, None)
                    population.append(unvacc_person)
        return population
    
    
    #This method should return True if the simulation
    # should continue, or False if it should not. The simulation should end under
    # any of the following circumstances:
    #     - The entire population is dead.
    #     - There are no infected people left in the population.
    # In all other instances, the simulation should continue.
    def _simulation_should_continue(self):
        # print("running sim_should_cont")

        # logic helped created by Jaeson! - https://github.com/jaebooker/virus_simulation/blob/master/simulation.py
        for person in self.population:
            # did_person_survive = person.did_survive_infection()
            # print("person.did_surv_infec: ",did_person_survive)
            # print("person alive:",person.is_alive)
            if not person.is_alive:
                self.total_dead += 1
        # Why is this 2?
        # print("CURRENT INFECTED:",self.current_infected)
        # print("POP:",len(self.population))
        # print("DEAD",self.total_dead)
        if (len(self.population)-self.total_dead) < 1:
            print("Everyone has died. The virus has ceased to spread.")
            return False
        elif self.current_infected == 0:
            print("The virus has ceased to spread. With a population of " + str(len(self.population)-self.total_dead) + " still alive.")
            return False        
            # print("currently infected: " + str(self.current_infected))
            # print("population remaining: " + str(len(self.population)-self.total_dead))
        return True

    def run(self):
        # print("running run")
        time_step_counter = 0
        # print("time step counter:",time_step_counter)
        should_continue = True
        while should_continue:
            # print("in while loop")
            # TODO: for every iteration of this loop, call self.time_step() to compute another
            # round of this simulation. At the end of each iteration of this loop, remember
            # to rebind should_continue to another call of self._simulation_should_continue()!
            self.time_step()
            # print("just called time_step")
            time_step_counter+=1
            # print("time_step_counter",time_step_counter)
            should_continue = self._simulation_should_continue()
            # print("should continue now = ", should_continue)
        print('The simulation has ended after time_step_counter: ',time_step_counter)
        # Log the stats
        # self.logger.stats(self.population, self.total_infected)

    def time_step(self):
        infectedPeople = [person for person in self.population if person.infected != None and person.is_alive]

        healthyAlivePeople = [person for person in self.population if not person.infected and person.is_alive]
        # for person in self.population:
        #     if person.infected is not None:
        #         print("Person is infected")
        #     else:
        #         print('Person is not infected')
        #     if person.is_alive:
        #         print("Person is alive!")
        #     else:
        #         print("Person is dead!")
        # print("infected people:",infectedPeople)
        for sickPerson in infectedPeople:
            # print('entered for loop')
            for i in range(0,100):
                # check if they're alive.
                randoInt = random.randint(0,len(healthyAlivePeople)-1)
                victim = healthyAlivePeople[randoInt]
                self.interaction(sickPerson, victim)
                # interaction+=1
                # Jaeson's Peer coding help to check to see if the Person survived the infection, and do the appropriate loggers for each case.
            if sickPerson.did_survive_infection(self.mortality_rate) == True:
                self.logger.log_infection_survival(sickPerson, True)
            if sickPerson.did_survive_infection(self.mortality_rate) == False:
                self.logger.log_infection_survival(sickPerson, False)
            
        self._infect_newly_infected()
   
    #This method should be called any time two living
    # people are selected for an interaction.  That means that only living people
    # should be passed into this method.  Assert statements are included to make sure
    # that this doesn't happen.
    def interaction(self, sickPerson, random_person):
        # print("interaction running!")
        if random_person.is_vaccinated == False:
            if random_person.is_alive == True:
                if random.random() < self.basic_repro_num:
                    self.newly_infected.append(random_person._id)
                    self.logger.log_interaction(sickPerson, random_person, True, False)
                else:
                    self.logger.log_interaction(sickPerson, random_person, False, False)
            else:
                self.logger.log_interaction(sickPerson, random_person, False, False)
        else:
            self.logger.log_interaction(sickPerson, random_person, False, True)
    
    def _infect_newly_infected(self):
        # print("newly infected:",self.newly_infected)
        sick_people_count=0
        for id in self.newly_infected:
            for person in self.population:
                if person._id == id and person.infected == None and person.is_alive == True:
                    sick_people_count+=1
                    person.infected = self.virus_name
        
        self.current_infected = sick_people_count
        self.total_infected += sick_people_count
        
        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    population_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, mortality_rate, basic_repro_num)
    simulation = Simulation(population_size, vacc_percentage, virus.virus_name, virus.mortality_rate, virus.basic_repro_num, initial_infected)
    simulation.run()
    simulation.logger.log_file.close()
