# agents/agent_core.py
from typing import Optional

class LLM_Agent_Core:
    """
    Base class to simulate an agent powered by an LLM (e.g., Gemini).
    """
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        # This print line helps with Observability/Logging
        print(f"[Core Init] {self.name} ready. Role: {self.system_prompt[:25]}...")

    def execute(self, task_input: str, tools: Optional[list] = None) -> str:
        """Simulates the LLM receiving context and executing a task/tool."""
        # This is a placeholder for the actual LLM API call
        return f"LLM execution success for {self.name} on input: {task_input[:15]}..."