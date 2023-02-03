import numpy as np

# https://www.kdnuggets.com/2023/01/introduction-markov-chains.html
# Define the states of the Markov chain
states = ["increasing", "decreasing", "stable"]

# Define the transition probabilities
transition_probs = np.array([[0.6, 0.3, 0.1], [0.4, 0.4, 0.2], [0.5, 0.3, 0.2]])

# Set the initial state
current_state = "increasing"

# Set the number of time steps to simulate
num_steps = 10

# Simulate the Markov chain for the specified number of time steps
for i in range(num_steps):
    # Get the probability of transitioning to each state
    probs = transition_probs[states.index(current_state)]
    
    # Sample a new state from the distribution
    new_state = np.random.choice(states, p=probs)
    
    # Update the current state
    current_state = new_state
    
    # Print the current state
    print(f"Step {i+1}: {current_state}")

