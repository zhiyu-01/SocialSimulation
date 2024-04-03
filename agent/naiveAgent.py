import asyncio
import queue
from agent.base import BaseAgent

class NaiveAgent(BaseAgent):
    def __init__(self, id, delay):
        super().__init__()
        self.id = id
        self.count = 0
        self.delay = delay
        self.activeflag = True
        self.inputflag = False
        self.outputflag = False
        self.inputqueue = queue.Queue()
        self.outputqueue = queue.Queue()
    
    async def _arun(self):
        while True:
            if self.activeflag:
                if self.inputflag:
                    await self.process_input()
                    self.inputflag = False
                self.count += 1
                self.outputqueue.put("第" + str(self.count) + "次发送消息。")
                self.outputflag = True
                await asyncio.sleep(self.delay)
    
    async def process_input(self):
        while not self.inputqueue.empty():
            content = self.inputqueue.get()
            print(f'Agent {self.id} 收到: {content}', end="")
    
    async def process_output(self, writer):
        if self.outputflag:
            while not self.outputqueue.empty():
                content = self.outputqueue.get()
                message = str(self.id) + "$%$" + content + '\n'
                writer.write(message.encode())
                await writer.drain()
                print(f'Agent {self.id} 发送: {content}')
                self.outputflag = False
    
    def get_id(self):
        return self.id