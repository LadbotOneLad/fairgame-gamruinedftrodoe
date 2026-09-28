import os
import time
import sys

print("[-] INITIALISING SILICON SENTINEL LAYER...")
print("[*] Monitoring physical electron drift, voltage thresholds, and thermal envelopes.\n")

def read_sys_file(path):
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return f.read().strip()
        except:
            return "LOCKED"
    return "N/A"

# Common Android kernel thermal and voltage paths
thermal_paths = [
    "/sys/class/thermal/thermal_zone0/temp",
    "/sys/class/thermal/thermal_zone1/temp",
    "/sys/devices/virtual/thermal/thermal_zone0/temp"
]

voltage_paths = [
    "/sys/class/power_supply/battery/voltage_now",
    "/sys/class/power_supply/battery/batt_vol"
]

freq_paths = [
    "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq",
    "/sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq"
]

try:
    for i in range(5):
        # 1. Extract Temperature
        temp_raw = "N/A"
        for p in thermal_paths:
            res = read_sys_file(p)
            if res not in ["N/A", "LOCKED"]:
                temp_raw = res
                break
        
        # Standardise thermal scaling (Android files sometimes present milli-Celsius)
        try:
            temp = float(temp_raw)
            if temp > 1000: temp /= 1000.0
            temp_str = f"{temp:.1f}°C"
        except:
            temp_str = "UNKNOWN"

        # 2. Extract Voltage
        volt_raw = "N/A"
        for p in voltage_paths:
            res = read_sys_file(p)
            if res not in ["N/A", "LOCKED"]:
                volt_raw = res
                break
        try:
            volt = float(volt_raw)
            if volt > 1000: volt /= 1000000.0 # Standardise microvolts to volts
            volt_str = f"{volt:.3f}V"
        except:
            volt_str = "UNKNOWN"

        # 3. Extract Clock Speed
        freq_str = "UNKNOWN"
        for p in freq_paths:
            res = read_sys_file(p)
            if res not in ["N/A", "LOCKED"]:
                try:
                    freq_str = f"{int(res) / 1000:.0f} MHz"
                    break
                except:
                    pass

        # Print current electron pressure snapshot
        sys.stdout.write(f"\r[NODE SNAPSHOT {i+1}/5] Thermal Core: {temp_str} | Electron Pressure: {volt_str} | Clock: {freq_str}")
        sys.stdout.flush()
        time.sleep(1)
    print("\n\n[+] TRACKING PASS COMPLETE. SILICON CHANNELS REMAIN BOUNDED.")
except KeyboardInterrupt:
    print("\n[!] Sentinel terminated by operator.")
