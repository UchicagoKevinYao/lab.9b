import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_empty_patch(self, world):
        options = [(self.x + dx, self.y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                   if (0 <= self.x + dx < world.size) and (0 <= self.y + dy < world.size)
                   and world.grid[self.x + dx][self.y + dy] is None]
        return random.choice(options) if options else None

    def move(self, new_position):
        self.x, self.y = new_position

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = []
        for _ in range(num_agents):
            while True:
                x, y = random.randint(0, size-1), random.randint(0, size-1)
                if self.grid[x][y] is None:
                    agent = Agent(x, y)
                    self.agents.append(agent)
                    self.grid[x][y] = agent
                    break

    def update(self):
        for agent in self.agents:
            new_position = agent.find_empty_patch(self)
            if new_position:
                self.grid[agent.x][agent.y] = None  
                agent.move(new_position)
                self.grid[new_position[0]][new_position[1]] = agent  
world_size = 5  
num_agents = 3  
num_steps = 10  

world = World(world_size, num_agents)

for step in range(num_steps):
    world.update()
    print(f"After step {step + 1}:")
    for agent in world.agents:
        print(f"Agent at ({agent.x}, {agent.y})")
