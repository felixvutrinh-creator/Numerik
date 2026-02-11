import numpy as np
import matplotlib.pyplot as plt
def _parse_float(s):
    s = s.strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None
    
v0 = _parse_float(input("Anfangsgeschwindigkeit v0 (m/s): "))

dt = _parse_float(input("Zeitschritte in Sekunden: "))  # Zeitschritt in Sekunden
t_max = _parse_float(input("Endzeit: "))
    

g = 9.81  # Erdbeschleunigung in m/s^2

# dv / dt = -g
# ds / dt = v 
    # Numerische Integration mit Euler-Verfahren
t = np.arange(0, t_max, dt)


# Leere Liste für Zeit

v = np.linspace(0, t_max, len(t))
v[0] = v0 

# Euler Verfahren
for i in range(1, len(t)):
    dv_dt = -g
    v[i] = v[i-1] + dv_dt * dt

print(v)

