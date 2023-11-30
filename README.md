# 2D-Dipole-Groundstate
Minimum total dipole-dipole energy interaction for a 2D crystal lattice

# Add more dipoles to the configuration
If you wish to add more dipoles, simply edit lines 32-40 to include additional ones. For example,

def objective(angles):
    theta1, theta2, theta3 = angles
    dipoles = [[np.cos(np.radians(theta1)), np.sin(np.radians(theta1))],
               [np.cos(np.radians(theta2)), np.sin(np.radians(theta2))],
               [np.cos(np.radians(theta3)), np.sin(np.radians(theta3))]]
    positions = [[0, 0], [1, 1],[0. 1]] #coordinates
    return total_energy_of_dipoles(dipoles, positions)
    
initial_angles = [np.random.randint(0, 360), np.random.randint(0, 360), np.random.randint(0, 360)]

# References

J. Batle,
Minimum energy configurations for interacting dipoles in simple hypercubic lattices,
Results in Physics,
Volume 16,
2020,
103114,
ISSN 2211-3797,
https://doi.org/10.1016/j.rinp.2020.103114.
(https://www.sciencedirect.com/science/article/pii/S2211379720306264)
Abstract: Systems consisting of dipoles owe their properties to the specific nature of the dipole-dipole interaction. Usually this form of interaction is intended for systems in three dimensions, although in several instances it can be reduced to 2+∊ dimensions. Their study is relevant because under certain conditions, such as large dipole moments or low temperatures, the classical approach is still valid in quantum systems. In the present work, we shall study systems of particles possessing a dipole moment arranged beyond the two-dimensional (three-dimensional) simple square (simple cubic) lattice. That is, we shall i) find the equilibrium configuration for dipoles in extended hypercubic lattices, and ii) compute the concomitant minimum energy per dipole in the bulk. Our approach shall not resort to any Ewald summation technique, is completely general and can be extended to any periodic geometric configuration. The corresponding results imply a slightly exponential scaling of the energy in terms of the dimension D itself.
Keywords: Dipole-dipole interaction; Minimum energy; Hypercubic lattices

