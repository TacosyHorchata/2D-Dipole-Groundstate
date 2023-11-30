# 2D-Dipole-Groundstate
Minimum total dipole-dipole energy interaction for a 2D crystal lattice

If you wish to add more dipoles, simply edit lines 32-40 to include additional ones. For example,

def objective(angles):
    theta1, theta2, theta3 = angles
    dipoles = [[np.cos(np.radians(theta1)), np.sin(np.radians(theta1))],
               [np.cos(np.radians(theta2)), np.sin(np.radians(theta2))],
               [np.cos(np.radians(theta3)), np.sin(np.radians(theta3))]]
    positions = [[0, 0], [1, 1],[0. 1]]
    return total_energy_of_dipoles(dipoles, positions)

# Valores iniciales para los angulos
initial_angles = [np.random.randint(0, 360), np.random.randint(0, 360), np.random.randint(0, 360)]

