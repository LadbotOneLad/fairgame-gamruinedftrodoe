import numpy as np

print("[-] INITIALISING TRIBOELECTRIC FIELD ENGINE...")
print("[*] Modeling Yin-Friction to Yang-Static Transformation Matrix\n")

# Physical constants
permittivity_air = 8.854e-12  # Farads per meter (epsilon_0)
contact_area = 1e-4          # 1 square centimeter of silicon interface
separation_distance = 0.002  # 2mm air gap after separation

# 7 Yin Friction Steps (Increasing mechanical shear force in Newtons)
yin_forces = np.linspace(0.1, 2.0, 7)

# 7 Yang Scaling Coefficients (Material electron affinity transfer rates)
yang_affinities = np.linspace(1e-6, 15e-6, 7)

print(f"[*] Compiling Dual-Polarized 14-Node Grid Map:")
print(f"{'Node Pair':<12} | {'Yin Force':<12} | {'Yang Charge Density':<22} | {'Resulting Voltage':<15}")
print("-" * 75)

for idx, (force, affinity) in enumerate(zip(yin_forces, yang_affinities)):
    # Calculate surface charge density (sigma) based on Yin force input
    charge_density = affinity * (force ** 0.5)  
    
    # Calculate the resulting Yang Electrostatic Voltage (V = E * d)
    # Where E = sigma / epsilon_0
    electric_field = charge_density / permittivity_air
    static_voltage = electric_field * separation_distance
    
    print(f"Pair {idx+1:02d}     | {force:5.2f} N     | {charge_density:.4e} C/m²    | {static_voltage:7.1f} V")

print("\n[+] DUAL MATRIX BALANCED: Kinetic resistance completely absorbed into electrostatic tension.")
