#  PID Control Interactive Simulation
#  Dynamic Systems Workshop – Dr. Wasel Ghanem & Fayzeh Elzghier

# =======================
#  Import Libraries
# =======================
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from ipywidgets import interact

# =======================
#  Define the plant (Second-order system)
# =======================
# G(s) = 1 / (s^2 + s + 1)
plant = ctrl.tf([1], [1, 1, 1])

# =======================
#  💡 Define PID Controller with selectable input type
# =======================
def pid_sim(Kp=1.0, Ki=0.0, Kd=0.0, signal_type='Step'):
    # PID Controller: C(s) = Kp + Ki/s + Kd*s
    C = ctrl.tf([Kd, Kp, Ki], [1, 0])
    
    # Closed-loop system
    sys_cl = ctrl.feedback(C * plant)
    
    # Time vector
    t = np.linspace(0, 10, 500)

    # Generate the input signal based on user choice
    if signal_type == 'Step':
        t_out, y_out = ctrl.step_response(sys_cl, t)
        u = np.ones_like(t)  # Step input
    elif signal_type == 'Ramp':
        u = t  # Ramp input
        t_out, y_out = ctrl.forced_response(sys_cl, T=t, U=u)
    elif signal_type == 'Sinusoidal':
        omega = 1.0  # frequency in rad/s
        u = np.sin(omega * t)
        t_out, y_out = ctrl.forced_response(sys_cl, T=t, U=u)
    else:
        raise ValueError("Invalid signal type.")

    # Plot results
    plt.figure(figsize=(8,4))
    plt.plot(t_out, y_out, label="System Output", linewidth=2)
    plt.plot(t, u, '--', label=f"{signal_type} Input", alpha=0.7)
    plt.title(f"{signal_type} Response | Kp={Kp}, Ki={Ki}, Kd={Kd}")
    plt.xlabel("Time (s)")
    plt.ylabel("Output y(t)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

# =======================
#  🔄 Interactive Controls
# =======================
print("🎛️ Adjust the sliders and input type to observe PID behavior:\n")

interact(
    pid_sim,
    Kp=(0.0, 10.0, 0.5),
    Ki=(0.0, 5.0, 0.2),
    Kd=(0.0, 3.0, 0.1),
    signal_type=['Step', 'Ramp', 'Sinusoidal']
);

# =======================
#  💬 Observations
# =======================
print("""
💡 Hints for analysis:
- Increase Kp → faster response but more oscillation.
- Increase Ki → removes steady-state error but may cause overshoot.
- Increase Kd → adds damping and reduces overshoot.

📈 Try switching between Step, Ramp, and Sinusoidal inputs to visualize:
- Tracking capability (Ramp)
- Steady-state error
- Phase lag and oscillation (Sinusoidal)
""")
