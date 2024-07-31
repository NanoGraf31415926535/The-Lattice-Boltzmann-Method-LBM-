# Lattice Boltzmann Simulation with Cylinder Obstacle

This project simulates fluid flow around a cylindrical obstacle using the Lattice Boltzmann Method (LBM). The simulation visualizes both the velocity magnitude and the curl of the velocity field, updating dynamically in a single window.

## Description

The Lattice Boltzmann Method is a numerical algorithm for fluid dynamics simulation. This code initializes a 2D grid with a cylindrical obstacle and simulates the fluid flow over time, visualizing the results using Matplotlib.

## Key Concepts

### Lattice Boltzmann Method

The LBM operates on a discrete grid (lattice) and evolves the fluid's particle distribution functions over time. The core components include:

1. **Lattice Velocities and Weights**: Defines the discrete directions and their associated weights.
   \[
   c_i = (c_{x_i}, c_{y_i}), \quad w_i
   \]
   
2. **Distribution Function**: \( F(x, t) \) represents the distribution of particles at position \( x \) and time \( t \).

3. **Macroscopic Variables**: The density \( \rho \) and velocity \( \mathbf{u} \) are obtained from the distribution functions:
   \[
   \rho = \sum_i F_i
   \]
   \[
   \mathbf{u} = \frac{1}{\rho} \sum_i F_i \mathbf{c}_i
   \]

4. **Equilibrium Distribution Function**: \( F_i^{eq} \) ensures that the system evolves towards equilibrium.
   \[
   F_i^{eq} = \rho w_i \left(1 + 3 \frac{\mathbf{c}_i \cdot \mathbf{u}}{c_s^2} + \frac{9}{2} \left(\frac{\mathbf{c}_i \cdot \mathbf{u}}{c_s^2}\right)^2 - \frac{3}{2} \frac{\mathbf{u} \cdot \mathbf{u}}{c_s^2} \right)
   \]
   where \( c_s \) is the speed of sound.

5. **Collision and Streaming Steps**: The LBM alternates between local collisions and propagation of particles:
   \[
   F_i(x + c_i \Delta t, t + \Delta t) = F_i(x, t) - \frac{1}{\tau} \left(F_i(x, t) - F_i^{eq}(x, t)\right)
   \]

### Visualization

The simulation visualizes:
- **Velocity Magnitude**: The magnitude of the fluid velocity field.
- **Curl**: The curl (or vorticity) of the velocity field, indicating rotational motion in the fluid.

## Code Overview

### Dependencies

- NumPy: For numerical operations.
- Matplotlib: For plotting the simulation results.

### Main Components

1. **Initialization**:
   - Defines the grid size, lattice speeds, weights, and initial conditions.
   - Creates a cylindrical obstacle in the grid.

2. **Main Loop**:
   - Executes the LBM steps for a specified number of iterations.
   - Updates the velocity field and enforces boundary conditions.
   - Computes equilibrium distribution functions and performs the collision step.
   - Updates the plots with velocity magnitude and curl.

3. **Visualization**:
   - Uses Matplotlib to create two subplots for velocity magnitude and curl.
   - Updates the plots dynamically to reflect the simulation progress.
   - Adds colorbars and iteration index text to the plots.

### Example Output

![Figure_1](https://github.com/user-attachments/assets/ada06212-409b-495c-9662-bb3bbd95bba0)


## Running the Code

To run the simulation:

1. Ensure you have the required dependencies installed:
pip install numpy matplotlib


2. Execute the Python script:

The simulation will display a window with two plots updating dynamically: one for velocity magnitude and one for curl.

## Author

This code was written by Artem Sakhniuk.

## Credits

The code was writen by inspiring with this articles, make sure you understand what's happening 
https://www.simscale.com/docs/simwiki/cfd-computational-fluid-dynamics/lattice-boltzmann-method-lbm/
https://medium.com/swlh/create-your-own-lattice-boltzmann-simulation-with-python-8759e8b53b1c

