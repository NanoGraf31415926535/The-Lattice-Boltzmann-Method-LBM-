import numpy as np
from matplotlib import pyplot as plt

plot_every = 100

def distances(x1, x2, y1, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

def main():

    Nx = 400
    Ny = 100
    tau = .53
    Nt = 20000

    # Lattice speeds and weights 
    NL = 9
    cxs = np.array([0,0,1,1,1,0,-1,-1,-1])
    cys = np.array([0,1,1,0,-1,-1,-1,0,1])
    weights = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36])

    # Initial Conditions 
    F = np.ones((Ny, Nx, NL)) + .01 * np.random.randn(Ny, Nx, NL)
    F[:, :, 3] = 2.3

    # Create a cylinder with boundary conditions
    cylinder = np.full((Ny, Nx), False)

    for y in range(Ny):
        for x in range(Nx):
            if distances(Nx//4, x, Ny//2, y) < 13:
                cylinder[y, x] = True

    # Initialize the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    im1 = ax1.imshow(np.zeros((Ny, Nx)), cmap='bwr')
    im2 = ax2.imshow(np.zeros((Ny, Nx)), cmap='bwr')
    ax1.set_title('Velocity Magnitude')
    ax2.set_title('Curl')
    cbar1 = plt.colorbar(im1, ax=ax1)
    cbar2 = plt.colorbar(im2, ax=ax2)
    plt.ion()
    plt.show()

    # Main loop
    for it in range(Nt):  # We are iterating through time 
        print(it)

        F[:, -1, [6, 7, 8]] = F[:, -2, [6, 7, 8]]
        F[:, 0, [2, 3, 4]] = F[:, 1, [2, 3, 4]]

        for i, cx, cy in zip(range(NL), cxs, cys):
            F[:, :, i] = np.roll(F[:, :, i], cx, axis=1)
            F[:, :, i] = np.roll(F[:, :, i], cy, axis=0)

        # Fluid variables 
        rho = np.sum(F, axis=2)
        ux = np.sum(F * cxs, axis=2) / rho
        uy = np.sum(F * cys, axis=2) / rho

        # Enforce boundary conditions
        bndryF = F[cylinder, :]
        bndryF = bndryF[:, [0, 5, 6, 7, 8, 1, 2, 3, 4]]
        F[cylinder, :] = bndryF
        ux[cylinder] = 0
        uy[cylinder] = 0

        # Collision step
        Feq = np.zeros(F.shape)
        for i, cx, cy, w in zip(range(NL), cxs, cys, weights):
            Feq[:, :, i] = rho * w * (1 + 3 * (cx*ux + cy*uy) + 9 * (cx*ux + cy*uy)**2 / 2 - 3 * (ux**2 + uy**2) / 2)
        F += -(1/tau) * (F - Feq)

        if (it % plot_every == 0):
            velocity_magnitude = np.sqrt(ux**2 + uy**2)
            dfydx = ux[2:, 1:-1] - ux[0:-2, 1:-1]
            dfxdy = uy[1:-1, 2:] - uy[1:-1, 0:-2]
            curl = dfydx - dfxdy

            im1.set_data(velocity_magnitude)
            im2.set_data(curl)

            im1.set_clim(vmin=np.min(velocity_magnitude), vmax=np.max(velocity_magnitude))
            im2.set_clim(vmin=np.min(curl), vmax=np.max(curl))

            plt.pause(0.01)

if __name__ == "__main__":
    main()