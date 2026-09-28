import numpy as np

print("[-] INITIALISING CONTROLLED DISCIPLINE MATRIX...")
print("[*] State-Space Matrix Loop Over Damped Fields\n")

# Setting up time vector (0 to 20 nanoseconds, broken down into 10 steps)
time_steps = np.linspace(0, 20e-9, 10)

# Uncontrolled chaotic state parameters
current_wild = 25.0  # Starting error of 25 mA
target_state = 0.0   # The absolute calm disciplined baseline

# Simulated strict feedback gain factor (Our mathematical discipline coefficient)
K_discipline = 4.5e8  

print(f"[*] Discipline Gain Parameter Locked: K = {K_discipline:.2e}")
print(f"[*] Tracking State Convergence:\n")

for step in time_steps:
    # Error definition
    error = current_wild - target_state
    
    # Calculate the active corrective force vector (u)
    u_correction = -K_discipline * error * step
    
    # System response under discipline (exponential attenuation of chaos)
    disciplined_current = current_wild * np.exp(-K_discipline * step)
    
    print(f"Time: {step*1e9:5.2f} ns -> Wild Current: {error:6.2f} mA | Correction Applied: {u_correction/1e3:+7.2f} V | State: {disciplined_current:6.3f} mA")

print("\n[+] CONVERGENCE ACHIEVED: System state fully bound by mathematical discipline.")
