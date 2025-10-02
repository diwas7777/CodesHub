import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from lightkurve import search_lightcurve
from astropy.timeseries import LombScargle
import rebound

# 1. TRANSIT METHOD (Light Curve Analysis)
def analyze_light_curve(target='Kepler-10', mission='Kepler'):
    lc = search_lightcurve(target, mission=mission).download().normalize()
    time, flux = lc.time.value, lc.flux.value
    
    # Find dips in brightness
    peaks, _ = find_peaks(-flux, height=0.001)
    
    # Plot
    plt.figure(figsize=(10,4))
    plt.plot(time, flux, label='Light Curve')
    plt.plot(time[peaks], flux[peaks], 'ro', label='Detected Dips')
    plt.xlabel('Time (days)')
    plt.ylabel('Normalized Flux')
    plt.legend()
    plt.show()

# 2. RADIAL VELOCITY METHOD
def analyze_radial_velocity(time, velocity):
    # Input validation
    time = np.asarray(time)
    velocity = np.asarray(velocity)
    if time.ndim != 1 or velocity.ndim != 1:
        raise ValueError("Both 'time' and 'velocity' must be 1-dimensional sequences.")
    if time.shape[0] != velocity.shape[0]:
        raise ValueError("'time' and 'velocity' must have the same length.")
    frequency, power = LombScargle(time, velocity).autopower()
    
    plt.figure(figsize=(10,4))
    plt.plot(frequency, power)
    plt.xlabel('Frequency (1/days)')
    plt.ylabel('Power')
    plt.title('Radial Velocity Periodogram')
    plt.show()

# 3. ORBITAL PERTURBATIONS (Hidden Planet Detection)
def simulate_orbital_perturbations(simulation_time=1e3):
    sim = rebound.Simulation()
    sim.add(m=1.0)  # Star (mass in solar masses)
    sim.add(m=1e-3, a=1.0)  # Known planet
    sim.add(m=5e-4, a=1.7)  # Potential hidden planet
    
    sim.integrate(simulation_time)  # Simulate for simulation_time years
    
    particles = sim.particles
    for i, p in enumerate(particles):
        print(f'Object {i}: a={p.a}, e={p.e}, i={p.inc}')

# Example Usage
# analyze_light_curve()
# analyze_radial_velocity(time_data, velocity_data)  # Provide real dataset
# simulate_orbital_perturbations()
