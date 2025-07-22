import vpython

class creature:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.radius = 0.5
        self.selfObject = vpython.sphere(pos=vpython.vector(*location), radius=self.radius, color=vpython.color.red)

    def move(self, new_location):
        # Adjust bounds to account for the radius of the sphere
        clamped_location = (
            max(self.radius, min(new_location[0], 10 - self.radius)),  # Clamp X to [radius, 10 - radius]
            max(self.radius, min(new_location[1], 10 - self.radius)),  # Clamp Y to [radius, 10 - radius]
            max(self.radius, min(new_location[2], 10 - self.radius))   # Clamp Z to [radius, 10 - radius]
        )
        self.location = clamped_location
        self.selfObject.pos = vpython.vector(*self.location)  # Update the visual position
        print(f"{self.name} moved to {self.location}")

    def up(self):
        self.move((self.location[0], self.location[1] + 1, self.location[2]))
    def down(self):
        self.move((self.location[0], self.location[1] - 1, self.location[2]))
    def left(self):
        self.move((self.location[0] - 1, self.location[1], self.location[2]))
    def right(self):
        self.move((self.location[0] + 1, self.location[1], self.location[2]))
    def forward(self):
        self.move((self.location[0], self.location[1], self.location[2] + 1))
    def backward(self):
        self.move((self.location[0], self.location[1], self.location[2] - 1))

class grid:
    def __init__(self):
        self.creatures = []
        self.size = (10, 10, 10)  # Example grid size (x, y, z)
        self.grid_initialized = False  # Track if the grid has been drawn

    def add_creature(self, creature):
        self.creatures.append(creature)
        print(f"{creature.name} added to the grid at {creature.location}")

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
            if not (creature.selfObject.pos.x < radius or creature.selfObject.pos.x > self.size[0] - radius or 
                    creature.selfObject.pos.y < radius or creature.selfObject.pos.y > self.size[1] - radius or 
                    creature.selfObject.pos.z < radius or creature.selfObject.pos.z > self.size[2] - radius):
                creature.selfObject.pos = vpython.vector(*creature.location)
            else:
                # Set the creature back in bounds considering its radius
                creature.location = (
                    max(radius, min(self.size[0] - radius, creature.selfObject.pos.x)),
                    max(radius, min(self.size[1] - radius, creature.selfObject.pos.y)),
                    max(radius, min(self.size[2] - radius, creature.selfObject.pos.z))
                )
                creature.selfObject.pos = vpython.vector(*creature.location)
                print(f"{creature.name} was out of bounds and has been reset to {creature.location}.")