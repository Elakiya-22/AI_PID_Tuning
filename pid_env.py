import gymnasium as gym
from gymnasium import spaces
import numpy as np


class PIDEnv(gym.Env):

    def __init__(self):
        super(PIDEnv, self).__init__()

        # Action Space
        # Agent chooses Kp, Ki, Kd
        self.action_space = spaces.Box(
            low=np.array([0.0, 0.0, 0.0]),
            high=np.array([20.0, 5.0, 10.0]),
            dtype=np.float32
        )

        # Observation Space
        # [error, integral_error, derivative_error]
        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(3,),
            dtype=np.float32
        )

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.error = 1.0
        self.integral_error = 0.0
        self.derivative_error = 0.0

        observation = np.array([
            self.error,
            self.integral_error,
            self.derivative_error
        ], dtype=np.float32)

        return observation, {}

    def step(self, action):

        kp, ki, kd = action

        # Simple PID effect simulation
        control_output = (
            kp * self.error
            + ki * self.integral_error
            + kd * self.derivative_error
        )

        # Simulate system response
        new_error = self.error - 0.01 * control_output

        self.integral_error += new_error

        self.derivative_error = new_error - self.error

        self.error = new_error

        observation = np.array([
            self.error,
            self.integral_error,
            self.derivative_error
        ], dtype=np.float32)

        # Reward
        reward = -abs(self.error)

        terminated = abs(self.error) < 0.01

        truncated = False

        info = {}

        return observation, reward, terminated, truncated, info