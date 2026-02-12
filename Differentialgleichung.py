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
s0 = _parse_float(input("Anfangshöhe s0 (m): "))
dt = _parse_float(input("Zeitschritte in Sekunden: "))  # Zeitschritt in Sekunden
t_max = _parse_float(input("Endzeit: "))
    

g = 9.81  # Erdbeschleunigung in m/s^2

# dv / dt = -g
# ds / dt = v 
    # Numerische Integration mit Euler-Verfahren
t = np.arange(0, t_max, dt)

for i in range(len(t)):
    t[i] = t[i-1] + dt if i > 0 else 0
    pass
# Berechnung der Positionen und Geschwindigkeiten


# Leere Liste für Zeit

v = np.linspace(0, t_max, len(t))
s = np.linspace(0, t_max, len(t))
v[0] = v0 
s[0] = s0
# Euler Verfahren
for i in range(1, len(t)):
    dv_dt = -g
    v[i] = v[i-1] + dv_dt * dt
    s[i] = s[i-1] + v[i-1] * dt

if v[i] is 0:
    print("höchster Punkt bei:", t,s)    
print("Zeitpunkte:", t)
print("Geschwindigkeiten:", v)
print("Positionen:", s)

# Höchster Punkt Ausgabe
# v[i] muss = 0

for i in range(1, len(t)):
    if v[i-1] > 0 and v[i] <= 0:
        print("höchster Punkt bei:", t[i],s[i])
        plt.scatter(t[i],s[i])

# Wo liegt der HS auf dem Boden
# s[i]=0
for i in range(1, len(t)):
    if s[i-1] > 0 and s[i] <=0:
        print("Boden fällt bei:", t[i],s[i])
        plt.scatter(t[i],s[i])        
# Plotten der Flugbahn

plt.plot(t, s, label="Position s(t)")
plt.title("Position über die Zeit")
plt.xlabel("Zeit (s)")
plt.ylabel("Position (m)")
plt.legend()

plt.xlim(-20,20)
plt.ylim(-20,20)
plt.axhline(0)

plt.grid()
plt.show()
