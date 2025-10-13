# Test the solar system physics calculations
from solar_physics import *

# Create a simple star and planet system
star = Star()
star.m = 100000000000000000000000  # Very massive star
star.x = 0
star.y = 0
star.Vx = 0
star.Vy = 0

planet = Planet()
planet.m = 10000000000000000000  # Less massive planet
planet.x = 100
planet.y = 0
planet.Vx = 0
planet.Vy = 10000  # Moving in the y direction

# Test force calculation
objects = [star, planet]
calculate_force(planet, objects)
print(f"Force on planet: Fx={planet.Fx}, Fy={planet.Fy}")

# Test movement
dt = 1  # 1 second time step
move_space_object(planet, dt)
print(f"Planet position after 1s: x={planet.x}, y={planet.y}")
print(f"Planet velocity after 1s: Vx={planet.Vx}, Vy={planet.Vy}")

# Test angular velocity calculation
angular_velocity = calculate_angular_velocity(planet, star)
print(f"Angular velocity: {angular_velocity}")
