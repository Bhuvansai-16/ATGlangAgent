# dag.py

import logging
from node import UserInputNode, Agent, MemoryNode, JudgeNode

class DebateDAG:
    def __init__(self):
        # Initialize nodes
        self.user_input_node = UserInputNode()
        self.agent_a = Agent(name="Scientist", persona="Scientist")
        self.agent_b = Agent(name="Philosopher", persona="Philosopher")
        self.memory_node = MemoryNode()
        self.judge_node = JudgeNode()

        # Setup logger
        logging.basicConfig(filename='log.txt', level=logging.INFO, filemode='w')
        self.logger = logging.getLogger()

    def run(self):
        topic = self.user_input_node.get_topic()
        self.logger.info(f"Debate Topic: {topic}")

        print(f"\nStarting debate between {self.agent_a.name} and {self.agent_b.name}...\n")

        num_rounds = 8
        for round_num in range(1, num_rounds + 1):
            if round_num % 2 != 0:
                speaker = self.agent_a
            else:
                speaker = self.agent_b

            agent_memory = self.memory_node.get_agent_memory(speaker.name)
            argument = speaker.make_argument(topic, agent_memory)

            self.memory_node.update(speaker.name, argument)

            print(f"[Round {round_num}] {speaker.name}: {argument}")
            self.logger.info(f"[Round {round_num}] {speaker.name}: {argument}")

        # Judge phase
        summary, winner, reason = self.judge_node.judge(self.memory_node.transcript)

        print("\n[Judge] Summary of debate:")
        print(summary)
        print(f"\n[Judge] Winner: {winner}")
        print(f"Reason: {reason}")

        self.logger.info("\n[Judge] Summary of debate:")
        self.logger.info(summary)
        self.logger.info(f"\n[Judge] Winner: {winner}")
        self.logger.info(f"Reason: {reason}")
