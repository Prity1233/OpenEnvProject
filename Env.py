class DeliveryEnv:

    def _init_(self):
        self.state = "START"
        self.steps = 0

    def reset(self):
        self.state = "START"
        self.steps = 0
        return self.state

    def step(self, action):
        self.steps += 1

        # Invalid action
        if action not in ["pick", "move", "deliver"]:
            return self.state, -5, False

        # START state
        if self.state == "START":
            if action == "pick":
                self.state = "PICKED"
                reward = 0.5
            else:
                reward = -1

        # PICKED state
        elif self.state == "PICKED":
            if action == "move":
                self.state = "ON_THE_WAY"
                reward = 0.5
            else:
                reward = -1

        # ON_THE_WAY state
        elif self.state == "ON_THE_WAY":
            if action == "deliver":
                self.state = "DELIVERED"
                reward = 1
            else:
                reward = -1

        else:
            reward = 0

        done = self.state == "DELIVERED"

        # Step limit
        if self.steps > 5:
            done = True
            reward = -2

        return self.state, reward, done


# ---------------- TEST RUN ----------------

env = DeliveryEnv()

print("Reset:", env.reset())

print(env.step("pick"))      # Easy
print(env.step("move"))      # Medium
print(env.step("deliver"))   # Complete