# Help Creating Functions from Jaycee - https://github.com/jayceazua/herd_immunity/
from person import Person
from simulation import Simulation
import random
import pytest
random.seed(42)

def create_person():
    person = Person(0, True)
    return person

def test_create_person():
    person = create_person()
    person_2 = Person(1, False, None)
    assert person._id == 0
    assert person_2._id == 1
    assert person.is_alive == True
    assert person_2.is_alive == True
    assert person.is_vaccinated == True
    assert person_2.is_vaccinated == False
    assert person.infected == None
    assert person_2.infected == None