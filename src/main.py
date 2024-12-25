import numpy as np
import matplotlib.pyplot as plt
import rebound
from astropy import units as u
import math
import sys

from get_horizons_cache import cache_body

cache_body("Sun")
cache_body("Mercury")
cache_body("Venus")
cache_body("Earth")
cache_body("Mars")
cache_body("Jupiter")
cache_body("Saturn")
cache_body("Uranus")
cache_body("Neptune")
cache_body("Pluto")

sys.exit(0)

sim = rebound.Simulation()


sim.add("Sun")
sun = sim.particles[0]
sim.save_to_file("cache/sun.bin")
print(sun.m)
mercury = rebound.Particle("Mercury")
venus = rebound.Particle("Venus")
sim.add(sun)
sim.add(mercury, primary=sun)
sim.add(venus, primary=sun)
op = rebound.OrbitPlot(sim)
plt.show()
