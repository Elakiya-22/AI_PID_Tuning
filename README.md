# AI-Based PID Controller Tuning using Reinforcement Learning

## Overview

This project implements a PID-controlled Mass-Spring-Damper system and explores Reinforcement Learning for automatic PID parameter tuning.

## Features

* Mass-Spring-Damper simulation
* PID Controller (Kp, Ki, Kd)
* Performance metrics:

  * Overshoot
  * Settling Time
  * Steady-State Error (SSE)
* CSV result generation
* Custom Gymnasium environment
* PPO-based Reinforcement Learning agent

## Technologies Used

* Python
* NumPy
* Matplotlib
* Pandas
* Gymnasium
* Stable-Baselines3

## Project Structure

* pid_simulation.py : PID simulation and metrics
* pid_env.py : RL environment
* train_rl.py : PPO training
* test_rl.py : Model testing

## Results

The project evaluates controller performance using Overshoot, Settling Time, and SSE and compares different PID configurations.

## How to Run

Install dependencies:

pip install -r requirements.txt

Run simulation:

python pid_simulation.py

Train PPO agent:

python train_rl.py

Test PPO agent:

python test_rl.py
# AI_PID_Tuning
