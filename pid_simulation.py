import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ==========================
# System Parameters
# ==========================
m = 1.0      # Mass
c = 2.0      # Damping
k = 5.0      # Spring Constant

# ==========================
# PID Parameters
# ==========================
kp = 10
ki = 0.5
kd = 3

# ==========================
# Simulation Settings
# ==========================
dt = 0.01
simulation_time = 10
steps = int(simulation_time / dt)

# Desired Position
setpoint = 1.0

# Initial Conditions
position = 0.0
velocity = 0.0

# PID Variables
integral = 0
prev_error = 0

# Data Storage
time_data = []
position_data = []
setpoint_data = []

# ==========================
# Simulation Loop
# ==========================
for i in range(steps):

    # PID Control
    error = setpoint - position

    integral += error * dt

    derivative = (error - prev_error) / dt

    control_force = (
        kp * error
        + ki * integral
        + kd * derivative
    )

    prev_error = error

    # System Dynamics
    acceleration = (
        control_force
        - c * velocity
        - k * position
    ) / m

    velocity += acceleration * dt
    position += velocity * dt

    # Save Data
    time_data.append(i * dt)
    position_data.append(position)
    setpoint_data.append(setpoint)


# ==========================
# PERFORMANCE METRICS
# ==========================

# Overshoot (%)
overshoot = max(0, (max(position_data) - setpoint) / setpoint * 100)

# Steady-State Error (SSE)
sse = abs(setpoint - position_data[-1])

# Settling Time (±2% band)
tolerance = 0.02 * setpoint
settling_time = simulation_time

for i in range(len(position_data)):
    if all(abs(y - setpoint) <= tolerance for y in position_data[i:]):
        settling_time = time_data[i]
        break

print("\n===== PERFORMANCE METRICS =====")
print(f"Overshoot      : {overshoot:.2f}%")
print(f"Settling Time  : {settling_time:.2f} sec")
print(f"SSE            : {sse:.6f}")



results = pd.DataFrame({
    "Kp": [kp],
    "Ki": [ki],
    "Kd": [kd],
    "Overshoot": [overshoot],
    "Settling_Time": [settling_time],
    "SSE": [sse]
})

results.to_csv("pid_results.csv", index=False)

print("Results saved to pid_results.csv")
plt.figure(figsize=(8,5))

plt.plot(time_data, position_data,
         label="System Output")

plt.plot(time_data, setpoint_data,
         '--',
         label="Setpoint")

plt.xlabel("Time (s)")
plt.ylabel("Position")

plt.title(
    f"PID Response\n"
    f"Overshoot={overshoot:.2f}%  "
    f"Settling={settling_time:.2f}s  "
    f"SSE={sse:.4f}"
)

plt.legend()
plt.grid(True)
plt.show()  