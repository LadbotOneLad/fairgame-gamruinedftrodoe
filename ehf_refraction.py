import numpy as np

print("[-] INITIALISING EHF MILLIMETRIC BEAM SIMULATOR...")
print("[*] Target Frequency: 60 GHz (V-Band, Wavelength: 5mm)")

# Hex values parsed correctly as integers using proper 0x prefixing
leaf_hashes = {
    "julia_ehf": 0x7a02,
    "merkle_engine": 0xc8e3,
    "merkle_manifest": 0xc150,
    "yinyang_matrix": 0x936d
}

# Max possible value for a 16-bit hex token (0xffff) to normalize fields
MAX_16BIT = float(0xffff)

print("\n[-] EXTRACTING NORMALISED DIALECTRIC DENSITIES:")
layers = []
for name, hex_val in sorted(leaf_hashes.items()):
    normalized_density = hex_val / MAX_16BIT
    layers.append(normalized_density)
    print(f"[*] Layer [{name:<15}] Density Matrix Weight: {normalized_density:.4f}")

incident_angle = 45.0  # Input beam strike at 45 degrees
print(f"\n[*] Incident Beam Angle: {incident_angle}°")
current_angle = incident_angle

# Iterate beam through the 4-tier Merkle Blob Matrix using Snell's Law over Complex Media
for idx, n_layer in enumerate(layers):
    # Mapping normalized weight to refractive index step (1.0 = vacuum/air)
    refractive_index = 1.0 + (n_layer * 0.45)
    
    rad_incident = np.radians(current_angle)
    sin_refract = np.sin(rad_incident) / refractive_index
    
    if sin_refract <= 1.0:
        new_angle = np.degrees(np.arcsin(sin_refract))
        phase_shift = (2 * np.pi / 0.005) * refractive_index * 0.002  # 2mm layer thickness
        print(f"[Layer_{idx}] Index: {refractive_index:.4f} -> Refracted Angle: {new_angle:.2f}° | Phase Shift: {phase_shift:.2f} rad")
        current_angle = new_angle
    else:
        print(f"[Layer_{idx}] Total Internal Reflection Matrix Triggered!")
        break

print("\n[+] SPECTRUM SIMULATION COMPLETE")
