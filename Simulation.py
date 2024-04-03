import asyncio
from agentmanager.AgentManager import AgentManager
from threadmanager.ThreadManager import ThreadManager

async def main():
    agentmanager = AgentManager(1000)
    agentmanager.creat()
    threadmanager = ThreadManager(agentmanager)
    await asyncio.gather(*[threadmanager.AgentThread(), threadmanager.SocialThread()])

if __name__ == "__main__":
    asyncio.run(main())