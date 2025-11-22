# agents/intake_agent.py
from agents.agent_core import LLM_Agent_Core
# We need to import the class from the services folder
from services.session_service import InMemorySessionService 

class RequirementIntakeAgent(LLM_Agent_Core):
    def __init__(self, session_service: InMemorySessionService):
        system_prompt = "You are the initial agent. Collect user constraints (diet, cuisine, days) and format them."
        super().__init__("Requirement Intake Agent", system_prompt)
        self.session_service = session_service

    def process_request(self, user_input: str, session_id: str) -> dict:
        """Simulates LLM parsing user input and saves the state (Session Memory)."""
        # LLM logic to parse the complex request into structured data
        constraints = {
            "dietary_goals": "High-Protein, Halal",
            "cuisine": "Indian",
            "days": 5,
            "avoid": ["seafood", "pork derivatives"]
        }
        
        # Demonstrates saving state/session memory
        self.session_service.save_state(session_id, {"constraints": constraints})
        return constraints