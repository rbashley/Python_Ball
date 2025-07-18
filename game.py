import vpython

class creature:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.selfObject = vpython.sphere(pos=vpython.vector(*location), radius=0.5, color=vpython.color.red)

    def move(self, new_location):
        self.location = new_location
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

    def add_creature(self, creature):
        self.creatures.append(creature)
        print(f"{creature.name} added to the grid at {creature.location}")

    def display(self):
        # Clear the scene
        vpython.scene.objects.clear()

        # Display the creatures
        for creature in self.creatures:
            if not (creature.selfObject.pos.x < 0 or creature.selfObject.pos.x > self.size[0] or 
                    creature.selfObject.pos.y < 0 or creature.selfObject.pos.y > self.size[1] or 
                    creature.selfObject.pos.z < 0 or creature.selfObject.pos.z > self.size[2]):
                creature.selfObject.pos = vpython.vector(*creature.location)
            else:
                # Set the creature back in bounds
                creature.location = (
                    max(0, min(self.size[0], creature.selfObject.pos.x)),
                    max(0, min(self.size[1], creature.selfObject.pos.y)),
                    max(0, min(self.size[2], creature.selfObject.pos.z))
                )
                creature.selfObject.pos = vpython.vector(*creature.location)
                print(f"{creature.name} was out of bounds and has been reset to {creature.location}.")
                

        # Display the cube grid
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