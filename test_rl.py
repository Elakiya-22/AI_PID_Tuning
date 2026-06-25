from stable_baselines3 import PPO
from pid_env import PIDEnv

# Load Environment
env = PIDEnv()

# Load Trained Model
model = PPO.load("pid_ppo_model")

obs, info = env.reset()

for _ in range(20):

    action, _ = model.predict(obs)

    obs, reward, terminated, truncated, info = env.step(action)

    print("Action (Kp,Ki,Kd):", action)
    print("Error:", obs[0])
    print("Reward:", reward)

    if terminated:
        print("Target reached!")
        break