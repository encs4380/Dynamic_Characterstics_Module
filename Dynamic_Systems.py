# 📘 Dynamic Systems Exploration
# Interactive Visualization for First and Second Order Systems
# Prepared for Faiza 

# =======================
# 🧩 Import Libraries
# =======================
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from ipywidgets import interact

# =======================
# ⚙️ First-Order System
# =======================
# G(s) = K / (τs + 1)
def first_order(K=1.0, tau=1.0, signal_type='Step'):
    sys = ctrl.tf([K], [tau, 1])
    t = np.linspace(0, 10, 500)
    
    # Generate input signal
    if signal_type == 'Step':
        u = np.ones_like(t)
        t_out, y_out = ctrl.step_response(sys, t)
    elif signal_type == 'Ramp':
        u = t
        t_out, y_out = ctrl.forced_response(sys, T=t, U=u)
    elif signal_type == 'Sinusoidal':
        omega = 1.0
        u = np.sin(omega * t)
        t_out, y_out = ctrl.forced_response(sys, T=t, U=u)
    else:
        raise ValueError("Invalid signal type.")
    
    # Plot input and output
    plt.figure(figsize=(8,4))
    plt.plot(t, u, 'g--', label="Input Signal")
    plt.plot(t_out, y_out, 'b', label="System Output")
    plt.title(f"First-Order Response | K={K}, τ={tau}, Signal={signal_type}")
    plt.xlabel("Time (s)")
    plt.ylabel("Output y(t)")
    plt.grid(True)
    plt.legend()
    plt.show()

print("✨ First-Order System: Move sliders and select signal type:")
interact(first_order, K=(0.5, 3.0, 0.5), tau=(0.2, 3.0, 0.2), 
         signal_type=['Step', 'Ramp', 'Sinusoidal']);

# =======================
#  Second-Order System
# =======================
# G(s) = ωₙ² / (s² + 2ζωₙs + ωₙ²)
def second_order(zeta=0.5, omega_n=2.0, signal_type='Step'):
    sys = ctrl.tf([omega_n**2], [1, 2*zeta*omega_n, omega_n**2])
    t = np.linspace(0, 10, 500)
    
    # Generate input signal
    if signal_type == 'Step':
        u = np.ones_like(t)
        t_out, y_out = ctrl.step_response(sys, t)
    elif signal_type == 'Ramp':
        u = t
        t_out, y_out = ctrl.forced_response(sys, T=t, U=u)
    elif signal_type == 'Sinusoidal':
        omega = 1.0
        u = np.sin(omega * t)
        t_out, y_out = ctrl.forced_response(sys, T=t, U=u)
    else:
        raise ValueError("Invalid signal type.")
    
    # Plot input and output
    plt.figure(figsize=(8,4))
    plt.plot(t, u, 'g--', label="Input Signal")
    plt.plot(t_out, y_out, 'b', label="System Output")
    plt.title(f"Second-Order Response | ζ={zeta}, ωₙ={omega_n}, Signal={signal_type}")
    plt.xlabel("Time (s)")
    plt.ylabel("Output y(t)")
    plt.grid(True)
    plt.legend()
    plt.show()

print("\n💫 Second-Order System: Move sliders and select signal type:")
interact(second_order, zeta=(0.0, 2.0, 0.1), omega_n=(0.5, 5.0, 0.5), 
         signal_type=['Step', 'Ramp', 'Sinusoidal']);

# =======================
# 💡 Observations
# =======================
print("\n📚 Observations:")
print("- τ ↑ → first-order response slower.")
print("- ζ controls damping (oscillations) in second-order systems.")
print("- ωₙ controls speed in second-order systems.")
print("- K controls output level in first-order systems.")
print("- Ramp & Sinusoidal inputs let you explore tracking & oscillatory behavior.")
