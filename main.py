# main.py
import json
from typing import List, Dict
from datetime import date
from collections import deque

# Import Agents from the agents/ folder
from agents.agent_core import LLM_Agent_Core # Base class
from agents.intake_agent import RequirementIntakeAgent
from agents.generator_agent import RecipeGeneratorAgent
from agents.validator_agent import HalalValidatorAgent
from agents.compiler_agent import PlanCompilerAgent

# Import Services (Memory) from the services/ folder
from services.session_service import InMemorySessionService
from services.memory_bank import MemoryBank

def run_halal_chef(user_request: str, session_id: str = "user_123"):
    """
    Main function demonstrating the Sequential and Parallel Agent Workflow.
    This script coordinates all components of the multi-agent system.
    """
    print("🚀 Initializing Halal-Fit Chef Agent Workflow...")

    # 1. Initialize Services
    session_service = InMemorySessionService()
    memory_bank = MemoryBank()
    
    # Pre-populate MemoryBank for demonstration (Long Term Memory requirement)
    # The actual store_plan method is called below, but this ensures a favorite exists.
    memory_bank.store_plan({"recipes": [{"title": "High-Protein Lentil Curry"}], "date": "2025-10-01"}, rating=5)
    
    # 2. Initialize Agents
    intake_agent = RequirementIntakeAgent(session_service)
    generator_agent = RecipeGeneratorAgent()
    validator_agent = HalalValidatorAgent()
    compiler_agent = PlanCompilerAgent(memory_bank)

    print("\n--- STEP 1: Intake (Sequential Start) ---")
    
    # Step 1: Intake Agent collects constraints and saves state (Session Memory)
    constraints = intake_agent.process_request(user_request, session_id)
    print(f"✅ Constraints collected: {constraints}")

    # Load state check (demonstrates Sessions & State Management requirement)
    saved_state = session_service.load_state(session_id)
    print(f"✅ Session State Verified: {saved_state.get('constraints').get('dietary_goals')}")

    # --- STEP 2: Parallel Generation and Validation (Core Logic) ---
    print("\n--- STEP 2: Generation & Validation (Parallel Block) ---")
    
    # In a true system, these two lines run concurrently.
    # In this script, the data flow simulates the dependency:
    
    # 2a. Generator runs and calls Custom Tool (calculate_macros)
    generated_recipes = generator_agent.process_generation(constraints)
    print(f"⏳ Generator proposed {len(generated_recipes)} recipes.")

    # 2b. Validator runs and calls Built-in Tool (Google Search simulation)
    # Observability: Logs rejection reasons inside the validator agent.
    validated_recipes = validator_agent.process_validation(generated_recipes)
    print(f"✅ {len(validated_recipes)} recipes passed Halal validation.")

    # --- STEP 3: Compilation (Sequential End) ---
    print("\n--- STEP 3: Compiler Agent (Sequential End) ---")

    # Step 3: Compiler Agent uses validated recipes and Long Term Memory
    final_plan = compiler_agent.compile_plan(constraints, validated_recipes)
    
    print("\n################ WORKFLOW COMPLETE ################")
    print("FINAL PLAN SUMMARY:")
    # Print final output in readable JSON format
    print(json.dumps(final_plan, indent=2))
    
if __name__ == "__main__":
    # Example User Request (demonstrates complexity required for the project)
    USER_INPUT = "I need a 5-day, high-protein, Halal meal plan focused on Indian cuisine. Avoid seafood."
    run_halal_chef(USER_INPUT)