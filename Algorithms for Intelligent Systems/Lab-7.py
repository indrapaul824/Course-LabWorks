# Simple Hill Climbing Algorithm
def hill_climbing():
    # Define the initial state
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Define the goal state
    goal = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    # Define the number of iterations
    iterations = 0
    # Define the number of moves
    moves = 0
    # Loop until the goal is reached
    while state != goal:
        # Increment the number of iterations
        iterations += 1
        # Print the current state
        print(state)
        # Loop through the state
        for i in range(len(state)):
            # Check if the current state is the goal
            if state == goal:
                # Print the current state
                print(state)
                # Print the number of iterations
                print("Iterations: " + str(iterations))
                # Print the number of moves
                print("Moves: " + str(moves))
                # Exit the program
                exit()
            # Check if the current state is not the goal
            if state != goal:
                # Increment the number of moves
                moves += 1
                # Check if the current state is 0
                if state[i] != goal[i]:
# Run the hill climbing algorithm
hill_climbing()