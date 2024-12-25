import rebound


class NamedParticle(rebound.Particle):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name
        self.particle = parent


def cache_body(name):
    sim = rebound.Simulation()
    try:
        sim.add(name, hash=name)
        sim.save_to_file(f"cache/{name}.bin")
    except Exception as e:
        print("problem : ", e)


def get_cached_body(name) -> NamedParticle:
    try:
        sim = rebound.Simulation(f"cache/{name}.bin")
        particle = NamedParticle(sim.particles[0], name)

        return particle
    except Exception as e:
        print("problem : ", e)
        try:
            cache_body(name)
            sim = rebound.Simulation(f"cache/{name}.bin")
            particle = NamedParticle(sim.particles[0], name)
            return particle
        except Exception as e:
            print("problem : ", e)
            return None
