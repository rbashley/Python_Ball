import vpython
import numpy

class creature:
    def __init__(self, name, location, world):
        self.name = name
        self.world = world  # Reference to the world/grid
        self.heading = numpy.degrees(0)  # Initialize heading in degrees
        self.location = location
        self.radius = 0.5

        # Create the body as a red cube
        self.body = vpython.box(pos=vpython.vector(*location), size=vpython.vector(1, 1, 1), color=vpython.color.red)

    def forward(self, vector=1):
        # Move the creature forward in the direction of its heading
        self.world.handle_movement(self, vector)

    def backward(self, vector=-1):
        # Move the creature backward in the direction of its heading
        self.world.handle_movement(self, vector)

    def rotate(self, angle):
        # Rotate the creature's heading by the specified angle
        self.heading += angle

        if self.heading >= 360:
            self.heading -= 360
        elif self.heading < 0:
            self.heading += 360

        # Update the body orientation based on the new heading
        self.body.rotate(angle=numpy.radians(angle), axis=vpython.vector(0, 1, 0), origin=self.body.pos)

class grid:
    def __init__(self):
        self.creatures = []
        self.size = (10, 10, 10)  # Example grid size (x, y, z)
        self.grid_initialized = False  # Track if the grid has been drawn

    def add_creature(self, creature):
        self.creatures.append(creature)
        #print(f"{creature.name} added to the grid at {creature.location}")

    def handle_movement(self, creature, direction):
        # Calculate the movement vector based on the creature's heading
        heading_radians = numpy.radians(creature.heading)
        movement_vector = vpython.vector(
            direction * numpy.cos(heading_radians),  # X component
            0,  # Y component (no vertical movement in this example)
            direction * numpy.sin(heading_radians)   # Z component
        )

        # Update the creature's position
        new_position = vpython.vector(*creature.location) + movement_vector

        # Ensure the creature stays within the grid boundaries
        new_position.x = max(creature.radius, min(self.size[0] - creature.radius, new_position.x))
        new_position.y = max(creature.radius, min(self.size[1] - creature.radius, new_position.y))
        new_position.z = max(creature.radius, min(self.size[2] - creature.radius, new_position.z))

        # Update the creature's location and body position
        creature.location = (new_position.x, new_position.y, new_position.z)
        creature.body.pos = new_position

        # Print the new map position
        print(f"{creature.name} moved to map position {creature.location}")

    def display(self):
        if not self.grid_initialized:
            # Display the cube grid only once
            grid_center = vpython.vector(self.size[0] / 2, self.size[1] / 2, self.size[2] / 2)
            vpython.box(pos=grid_center, size=vpython.vector(*self.size), opacity=0.1)

            # Generate the 3D grid inside the cube using lines
            step = 1  # Step size for the grid lines
            for x in range(0, self.size[0] + 1, step):
                for y in range(0, self.size[1] + 1, step):
                    # Vertical lines
                    vpython.cylinder(pos=vpython.vector(x, y, 0) - grid_center, opacity=0.1, axis=vpython.vector(0, 0, self.size[2]), radius=0.01, color=vpython.color.blue)
                    # Horizontal lines (x-direction)
                    vpython.cylinder(pos=vpython.vector(x, 0, y) - grid_center, opacity=0.1, axis=vpython.vector(0, self.size[1], 0), radius=0.01, color=vpython.color.blue)
                    # Horizontal lines (y-direction)
                    vpython.cylinder(pos=vpython.vector(0, x, y) - grid_center, opacity=0.1, axis=vpython.vector(self.size[0], 0, 0), radius=0.01, color=vpython.color.blue)

            self.grid_initialized = True

        # Update the positions of creatures
        for creature in self.creatures:
            radius = creature.radius  # Use the creature's radius
            if not (creature.body.pos.x < radius or creature.body.pos.x > self.size[0] - radius or
                    creature.body.pos.y < radius or creature.body.pos.y > self.size[1] - radius or
                    creature.body.pos.z < radius or creature.body.pos.z > self.size[2] - radius):
                creature.body.pos = vpython.vector(*creature.location)
            else:
                # Set the creature back in bounds considering its radius
                creature.location = (
                    max(radius, min(self.size[0] - radius, creature.body.pos.x)),
                    max(radius, min(self.size[1] - radius, creature.body.pos.y)),
                    max(radius, min(self.size[2] - radius, creature.body.pos.z))
                )
                creature.body.pos = vpython.vector(*creature.location)
                #print(f"{creature.name} was out of bounds and has been reset to {creature.location}.")

    def add_nesw_markers(self, world_center):
        marker_distance = 12  # Distance from the center of the world
        marker_size = vpython.vector(1, 1, 1)  # Size of the markers

        # North marker (green)
        vpython.box(pos=world_center + vpython.vector(0, 0, marker_distance), size=marker_size, color=vpython.color.green)

        # East marker (red)
        vpython.box(pos=world_center + vpython.vector(marker_distance, 0, 0), size=marker_size, color=vpython.color.red)

        # South marker (blue)
        vpython.box(pos=world_center + vpython.vector(0, 0, -marker_distance), size=marker_size, color=vpython.color.blue)

        # West marker (yellow)
        vpython.box(pos=world_center + vpython.vector(-marker_distance, 0, 0), size=marker_size, color=vpython.color.yellow)