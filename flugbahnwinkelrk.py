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
k = _parse_float(input("Dämpfungskoeffizient k: "))
o = _parse_float(input("abwurfwinkel o: "))
g = 9.81  # Erdbeschleunigung in m/s^2

vx = v0 * np.cos(np.radians(o))  # Anfangsgeschwindigkeit in x-Richtung
vy = v0 * np.sin(np.radians(o))  # Anfangsgeschwindigkeit in y-Richtung

# Runege Kutta-Verfahren
t = np.arange(0, t_max, dt)
vy_rk4 = np.zeros(len(t))
vy_rk4[0] = vy
vx_rk4 = np.zeros(len(t))
vx_rk4[0] = vx 
sx = np.zeros(len(t))
sx[0] = 0
sy = np.zeros(len(t))
sy[0] = s0

# Kopffick

def dv_dt(t, v, g, k):
    return -g-k+v
def dvx_dt(t, vx, g, k):
    return -k*vx
def dvy_dt(t, vy, g, k):
    return -g-k*vy

def rk4_schrittx(t, vx, dt, g, k):
    kx1 = dvx_dt(t, vx, g, k)
    kx2 = dvx_dt(t+dt/2, vx+kx1*dt/2, g, k)
    kx3 = dvx_dt(t+dt/2, vx+ kx2*dt/2, g, k)
    kx4 = dvx_dt(t+ dt, vx+kx3*dt, g, k)

    vxneu = vx+(kx1+2*kx2+2*kx3+kx4)*dt/6
    return vxneu

def rk4_schritty(t, vy, dt, g,k):
    ky1 = dvy_dt(t, vy, g, k)
    ky2 = dvy_dt(t+dt/2,vy+ky1*dt/2, g,k)
    ky3 = dvy_dt(t+dt/2, vy+ ky2*dt/2, g, k)
    ky4 = dvy_dt(t+dt, vy+ky3*dt, g, k)

    vyneu = vy+(ky1+2*ky2+2*ky3+ky4)*dt/6
    return vyneu


for i in range(1, len(t)):
    vy_rk4[i] = rk4_schritty(t[i-1], vy_rk4[i-1], dt, g, k)
    
for i in range(1, len(t)):
    vx_rk4[i] = rk4_schrittx(t[i-1], vx_rk4[i-1], dt, g, k)

print (vx_rk4)
print (vy_rk4)

for i in range(1, len(t)):
    sx[i] = sx[i-1] + vx_rk4[i-1] * dt
for i in range(1, len(t)):
    sy[i] = sy[i-1] + vy_rk4[i-1] * dt        

print (sy)
print (sx)
# Rechnung fertig jetzt der andere Scheiß

# Wo ist der höchste Punkt ?


for i in range(1, len(t)):
    if vy_rk4[i-1] > 0 and vy_rk4[i] <=0:
        print("höchster Punkt bei", sx[i], sy[i])
        plt.scatter(sx[i], sy[i])

for i in range(1, len(t)):
    if sy[i-1] > 0 and sy[i] <=0:
        print("Objekt fällt bei:", sx[i], sy[i])
        plt.scatter(sx[i], sy[i])
# Plotten

plt.plot(sx, sy)
plt.gca().set_aspect('equal')
plt.title("Flugbahn eines Projektils mit Dämpfung")
plt.xlabel("Position in x-Richtung (m)")
plt.ylabel("Position in y-Richtung (m)")
plt.xlim(0, max(sx)*1.1)
plt.ylim(0, max(sy)*1.1)
plt.grid()
plt.show()       