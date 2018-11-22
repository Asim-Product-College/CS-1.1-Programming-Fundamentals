from virus import Virus
import unittest


def test_virus_instantiation():
    # * Check to make the virus instantiator is working 
    virus =  Virus("Ebola", 0.8, 0.3)
    assert virus.virus_name == "Ebola"
    assert virus.mortality_rate == 0.8
    assert virus.basic_repro_num