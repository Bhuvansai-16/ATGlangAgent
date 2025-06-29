# 🧠 Multi-Agent Debate DAG — LangGraph

This project is a **CLI-based debate simulation** built using **LangGraph**.  
It uses **two AI agents** (Scientist and Philosopher) to debate a user-specified topic in **8 structured rounds**, stores the debate memory, and runs a **Judge Node** to summarize the debate and declare a winner.

---

## 📌 **Project Overview**

**Key nodes in the debate DAG:**

- **UserInputNode:** Gets the debate topic from the user at runtime.
- **AgentA (Scientist):** Presents arguments from a scientific perspective.
- **AgentB (Philosopher):** Presents counterarguments from a philosophical perspective.
- **MemoryNode:** Stores the debate history and passes relevant context to each agent.
- **JudgeNode:** Summarizes the entire debate and declares a winner with justification.

---

## 🗂️ **File Structure**

```bash
debate/
├── main.py           # Entry point to run the debate flow (CLI)
├── dag.py            # Defines the DAG logic and execution loop
├── node.py           # Node definitions: UserInputNode, Agent, MemoryNode, JudgeNode
├── log.txt           # Auto-generated log of all debate arguments, memory states, and final verdict
├── dag_diagram.png   # Visual representation of the DAG (exported from draw.io)
├── .env              # Stores your API key for the LLM
├── requirements.txt  # Python dependencies (optional but recommended)
├── README.md         # This file

⚙️ How to Run
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your API key in .env:

env
Copy
Edit
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
Or for Gemini:

env
Copy
Edit
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
Run the CLI:

bash
Copy
Edit
python main.py
Enter the debate topic when prompted.
The debate will run automatically for 8 rounds, alternating between the Scientist and Philosopher.

Check the results:

All rounds, arguments, memory states, and the final verdict are displayed in the console.

The entire flow is also saved in log.txt.

📊 DAG Diagram
See dag_diagram.png for a clear view of the flow:

nginx
Copy
Edit
UserInputNode → AgentA → MemoryNode → AgentB → MemoryNode → JudgeNode

🧑‍⚖️ Judgment
The JudgeNode reviews the entire debate transcript and uses an LLM to produce:

A structured summary of key points.

A final winner based on argument strength.

A logical justification for the verdict.

✅ Deliverables
✔️ Fully working CLI app

✔️ Modular LangGraph nodes

✔️ Log file (log.txt)

✔️ DAG diagram (dag_diagram.png)

✔️ Demo video: Please see demo_video.mp4 or shared link for a 2–4 min walkthrough covering:

How to run the program

How the DAG works

The judgment logic


---