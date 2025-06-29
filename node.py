# nodes.py

class UserInputNode:
    def __init__(self):
        pass

    def get_topic(self):
        topic = input("Enter topic for debate: ")
        return topic



# nodes.py
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
from langchain_google_genai import ChatGoogleGenerativeAI

class Agent:
    def __init__(self, name, persona):
        self.name = name
        self.persona = persona
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

    def make_argument(self, topic, memory):
        transcript = "\n".join([f"{name}: {arg}" for name, arg in memory])
        prompt = (
            f"You are a {self.persona} debating the topic: {topic}.\n"
            f"Previous arguments:\n{transcript}\n"
            f"Write your next unique argument:"
        )
        response = self.llm.invoke(prompt)
        return response.content




class MemoryNode:
    def __init__(self):
        self.transcript = []
        self.summary = ""

    def update(self, agent_name, argument):
        self.transcript.append((agent_name, argument))

    def get_agent_memory(self, agent_name):
        # Could be more sophisticated: only relevant info
        return self.transcript


class JudgeNode:
    def __init__(self):
        pass

    def judge(self, transcript):
        # Placeholder logic: counts arguments, picks random winner
        summary = "\n".join([f"{name}: {arg}" for name, arg in transcript])
        winner = "Scientist"  # Placeholder
        reason = "Presented more grounded, risk-based arguments."
        return summary, winner, reason
