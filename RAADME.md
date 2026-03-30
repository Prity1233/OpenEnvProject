Delivery Environment (OpenEnv)

This project simulates a food delivery system.

States:
START → PICKED → ON_THE_WAY → DELIVERED

Actions:
pick, move, deliver

Rewards:
Correct action: +1 / +0.5
Wrong action: -1
Invalid action: -5

Run:
python Env.py