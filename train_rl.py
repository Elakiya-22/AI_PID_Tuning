from stable_baselines3 import PPO
from pid_env import PIDEnv

# Create Environment
env = PIDEnv()

# Create PPO Model
model = PPO(
    "MlpPolicy",
    env,
    verbose=1
)

# Train Model
model.learn(
    total_timesteps=10000
)

# Save Model
model.save("pid_ppo_model")

print("Training Complete!")
print("Model saved as pid_ppo_model")