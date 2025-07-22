import game
import vpython

def main():
    gameObj = game.grid()
    creature1 = game.creature("Creature1", (0, 0, 0))
    gameObj.add_creature(creature1)
    gameObj.display()

    # Define key bindings for movement
    def handle_keypress(evt):
        key = evt.key
        if key == 'w':
            creature1.forward()
        elif key == 's':
            creature1.backward()
        elif key == 'a':
            creature1.left()
        elif key == 'd':
            creature1.right()
        elif key == 'q':
            creature1.up()
        elif key == 'e':
            creature1.down()

    # Bind keys to the scene
    vpython.scene.bind('keydown', handle_keypress)

    # Run the program in a loop
    while True:
        vpython.rate(30)  # Limit the loop to 30 iterations per second
        gameObj.display()  # Continuously update the display

main()