from agent.naiveAgent import NaiveAgent

def timedelay(amount):
    import random

    weights = [0.05, 0.1, 0.15, 0.5, 0.1, 0.1]
    values = [0.5, 1, 2, 4, 8, 16]

    delays = random.choices(values, weights, k=amount)
    return delays

class AgentManager:
    def __init__(self, amount):
        self.amount = amount
        self.agents = []
        self.delays = timedelay(self.amount)

    def creat(self):
        for i in range(self.amount):
            agent = NaiveAgent(i, self.delays[i])
            self.add_agent(agent)

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def get_agents(self):
        return self.agents

    def get_agent(self, agent_id):
        for agent in self.agents:
            if agent.get_id() == agent_id:
                return agent
        return None