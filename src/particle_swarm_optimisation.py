"""
Particle Swarm Optimisation is a population based metaheuristic
- The state of the system at any given time is defined by the positions and velocities of all particles

How it works:
- starts with a population of particles with rand positions and velocities
- each particle is evaluated at their current position (fitness)
- we store a global best "gbest" and for a particle best "pbest"
- if a certain pbest is greater than gbest, we update gbest
- the velocity of each particle is calculated based on pbest, gbest, current velocity and rand values
-

"""


def particle_swarm_optimisation():
    print("Particle Swarm Optimisation")