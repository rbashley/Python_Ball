import game
import vpython

def main():
    gameObj = game.grid()
    creature1 = game.creature("Creature1", (5, 5, 5), gameObj)
    gameObj.add_creature(creature1)
    gameObj.display()

    # Add NESW markers to the world
    #worldObj = game.World(radius=10)  # Create a spherical world with radius 10
    gridObj = game.grid()
    gridObj.add_nesw_markers(vpython.vector(5, 5, 5))

    # Create a text area below the graphics window for readouts
    readout = vpython.wtext(text="\n")

    # Update the creature's methods to print to the readout
    def update_readout(message):
        readout.text = message

    # Define key bindings for movement
    def handle_keypress(evt):
        key = evt.key
        if key == 'w':
            creature1.forward()
        elif key == 's':
            creature1.backward()
        elif key == 'a':
            creature1.rotate(5)
        elif key == 'd':
            creature1.rotate(-5)

    # Bind keys to the scene
    vpython.scene.bind('keydown', handle_keypress)

    # Run the program in a loop
    while True:
        vpython.rate(30)  # Limit the loop to 30 iterations per second
        readout.text = f"{creature1.name} at position {creature1.location}, heading {creature1.heading} degrees"
        gameObj.display()  # Continuously update the display

main()