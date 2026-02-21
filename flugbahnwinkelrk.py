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
g = 9.81  # Erdbeschleunigung in m/s^2

vx = v0 * np.cos(np.radians(45))  # Anfangsgeschwindigkeit in x-Richtung
vy = v0 * np.sin(np.radians(45))  # Anfangsgeschwindigkeit in y-Richtung
# Runege Kutta-Verfahren
t = np.arange(0, t_max, dt)
vy_rk4 = np.zeros(len(t))
vy_rk4[0] = vy
vx_rk4 = np.zeros(len(t))
vx_rk4[0] = vx 
vy = np.linspace(0, t_max, len(t))
vx = np.linspace(0, t_max, len(t))
s = np.linspace(0, t_max, len(t))
vy[0] = vy
vx[0] = vx
s[0] = s0

# Kopffick

def dv_dt(t, v, g, k):
    return -g-k+v
def dvx_dt(t, vx, g, k):
    return 0
def dvy_dt(t, vy, g, k):
    return -g-k*vy

def rk4_schrittx(t, vx, dt, g, k):
    kx1 = dvx_dt(t, vx, g, k)
    kx2 = dvx_dt(t+dt/2, vx+kx1*dt/2, g, k)
    kx3 = dvx_dt(t+dt/2, v+ kx2*dt/2, g, k)
    kx4 = dvx_dt(t+ dt, v+kx3*dt, g, k)

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
    vy_rk4 = rk4_schritty(t[i-1], vy_rk4[i-1], dt, g, k)
    
