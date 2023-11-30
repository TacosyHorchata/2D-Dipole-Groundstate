from scipy.optimize import minimize
import numpy as np
    
def dipole_interaction_energy(m1, m2, pos1, pos2):
    #no utilizo epsilon, pero por si me sirve en el futuro xD
    epsilon_0 = 8.854187817e-12
    pos1 = np.array(pos1)
    pos2 = np.array(pos2)
    
    # distancia entre dipolos
    r = pos2 - pos1
    
    # modulo de la distancia entre los dipolos
    r_norm = np.linalg.norm(r)

    #formula de energia de interaccion entre 2 dipolos, considerando que sus momentos son iguales
    energy = ((np.dot(m1, m2) / r_norm**3) - (3*(np.dot(m1, r) * np.dot(m2, r))/r_norm**5))
   
    return energy

#suma de energias de interaccion entre todos los dipolos
def total_energy_of_dipoles(dipoles, positions):
    total_energy = 0
    for i in range(len(dipoles)):
        for j in range(i + 1, len(dipoles)):
            energy = dipole_interaction_energy(dipoles[i], dipoles[j], positions[i], positions[j])
            total_energy += energy
    return total_energy

def objective(angles):
    theta1, theta2 = angles
    dipoles = [[np.cos(np.radians(theta1)), np.sin(np.radians(theta1))],
               [np.cos(np.radians(theta2)), np.sin(np.radians(theta2))]]
    positions = [[0, 0], [1, 1]]
    return total_energy_of_dipoles(dipoles, positions)

# Valores iniciales para los angulos
initial_angles = [np.random.randint(0, 360), np.random.randint(0, 360)]

# Minimizar la funcion objective con el metodo gradiente conjugado
result = minimize(objective, initial_angles, method='CG')

optimized_angles = result.x
optimized_energy = result.fun
print("Optimized theta_1:", optimized_angles[0])
print("Optimized theta_2:", optimized_angles[1])
print("Energia del estado base:", optimized_energy)