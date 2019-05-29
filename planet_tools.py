'''
This file contains some example tools to do calculations with planets
'''
import numpy as np

average_density_kgpkm3 = 5.52e12 # kg/km^3 
planet_radii_km = {'mercury':2439, 'earth':6387, 'jupiter':71492} # km


def get_planet_mass_from_dictionary(planet, dictionary_of_radii, average_planet_density) :
  ''' Here is the docstring for this function that describes what it does.
  This uses a dictionary of radii whose keys are planet names to calculate a mass estimate of a planet.  
  '''
  radius_of_planet = dictionary_of_radii[planet]
  mass = 4./3 *np.pi*radius_of_planet**3 * average_planet_density 
  return mass

planet = input("ENter planet to get a mass out:")
print(get_planet_mass_from_dictionary(planet, planet_radii_km, average_density_kgpkm3))




# Exercise 1 : Transfer over the function get_planet_mass_from_dictionary to this python file.

# Hint:  You'll need to import numpy or math for pi.

# In a subsequent line, print out jupiter's "mass".  Hint, you'll need to define the variables that you feed into the function.

#  Goal, print out jupiter's "mass" the way we can print out "hello world..." below.  Things that need to go into this python module are the function definition and defined variables.
print('hello world in a script')
