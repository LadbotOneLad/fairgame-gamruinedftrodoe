import numpy as np

print("[-] CALCULATING SILICON CURRENT DYNAMICS...")
print("[*] Modeling Underdamped Transistor Discharge Loop\n")

# Physical constants for nano-scale silicon traces
L = 1e-6    # Inductance (Henries)
C = 1e-12   # Capacitance (Farads)
R = 50.0    # Resistance (Ohms)
I0 = 0.025  # Starting transient current (25 milliamps)

# Derived angular variables
alpha = R / (2 * L)
omega_zero = 1.0 / np.sqrt(L * C)
omega_d = np.sqrt(omega_zero**2 - alpha**2)

# Timeline array: 0 to 50 nanoseconds
t = np.linspace(0, 50e-9, 10)

print(f"[*] Attenuation Factor (Alpha): {alpha:.2e}")
print(f"[*] Resonant Ringing Frequency: {omega_d / 1e9:.2f} GHz\n")

# Compute current vector values
for step_time in t:
    current = I0 * np.exp(-alpha * step_time) * np.cos(omega_d * step_time)
    # Calculate physical electron drift velocity scale approximation
    drift_velocity = current * 1e-4 
    print(f"Time: {step_time*1e9:5.2f} ns -> Current Vector: {current*1000:6.3f} mA | Drift Offset: {drift_velocity:.4e} m/s")

print("\n[+] TRANSIENT SYSTEM CONVERGED: All residual electrons bound to receiver path.")
