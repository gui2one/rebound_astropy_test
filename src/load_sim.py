import matplotlib.pyplot as plt
import rebound
from get_horizons_cache import get_cached_body

sun = get_cached_body("Sun")
mercury = get_cached_body("Mercury")
venus = get_cached_body("Venus")
earth = get_cached_body("Earth")
mars = get_cached_body("Mars")
jupiter = get_cached_body("Jupiter")
saturn = get_cached_body("Saturn")
uranus = get_cached_body("Uranus")
neptune = get_cached_body("Neptune")
pluto = get_cached_body("Pluto")

sim = rebound.Simulation()

bodies = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
for body in bodies:
    sim.add(body.particle)


fig = rebound.OrbitPlot(sim, unitlabel="[AU]", color=True, periastron=True)

ax = fig.ax
for planet in bodies:
    ax.text(
        planet.particle.x,
        planet.particle.y,
        f"  {planet.name}",
        fontsize=8,
        ha="left",
        va="center",
    )
plt.show()
