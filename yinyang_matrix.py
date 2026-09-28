import hashlib
import cmath

# Initial core state derived from your genesis node
z_base = complex(-0.7, 0.27015)
c_const = complex(0.123, -0.456)

print("[-] INITIALIZING 14-NODE ROOT BALANCER...")
print(f"[*] Base Node: {z_base}\n")

# Mathematical definitions for the 14 Roots (7 Yin, 7 Yang)
yin_yang_formulas = [
    ("Yin-1 ", lambda z, c: cmath.sqrt(z - c)),
    ("Yang-1", lambda z, c: cmath.sqrt(z + c)),
    ("Yin-2 ", lambda z, c: cmath.log(z**2 - c) if (z**2 - c) != 0 else 0),
    ("Yang-2", lambda z, c: cmath.exp(cmath.tanh(z + c))),
    ("Yin-3 ", lambda z, c: cmath.asin(z / (c if c != 0 else 1))),
    ("Yang-3", lambda z, c: cmath.acos(z * c)),
    ("Yin-4 ", lambda z, c: (z**2 - c)**0.25),
    ("Yang-4", lambda z, c: (z**2 + c)**0.25),
    ("Yin-5 ", lambda z, c: cmath.tanh(z * c.conjugate())),
    ("Yang-5", lambda z, c: cmath.sinh(z * c.conjugate())),
    ("Yin-6 ", lambda z, c: 1.0 / cmath.sqrt(z**2 - c) if (z**2 - c) != 0 else 0),
    ("Yang-6", lambda z, c: 1.0 / cmath.sqrt(z**2 + c) if (z**2 + c) != 0 else 0),
    ("Yin-7 ", lambda z, c: z**3 - c),
    ("Yang-7", lambda z, c: z**3 + c)
]

master_pool = ""

# Execute matrix calculation and capture unique fingerprints
for name, formula in yin_yang_formulas:
    try:
        val = formula(z_base, c_const)
    except Exception:
        val = complex(0, 0)
        
    # Cast complex string vector into standard SHA-256 channel
    raw_bytes = str(val).encode('utf-8')
    node_hash = hashlib.sha256(raw_bytes).hexdigest()
    
    # Pool hashes for final master aggregation
    master_pool += node_hash
    print(f"[{name}] Vector: {str(val)[:28]:<28} -> Hash: {node_hash[:16]}...{node_hash[-8:]}")

# Generate the global synthetic root hash
master_hash = hashlib.sha256(master_pool.encode('utf-8')).hexdigest()
print(f"\n[+] SYNTHETIC ROOT HASH MATRIX COMPLETE")
print(f"[!] MASTER GENESIS KEY: {master_hash}")
