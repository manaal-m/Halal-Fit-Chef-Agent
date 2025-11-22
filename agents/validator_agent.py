# agents/validator_agent.py
from agents.agent_core import LLM_Agent_Core
# We need to import the Built-in Tool simulation
from tools.google_verifier import google_search_halal_verifier
from typing import List, Dict

class HalalValidatorAgent(LLM_Agent_Core):
    def __init__(self):
        system_prompt = "Critically check all recipe ingredients for Halal compliance. Use Google Search tool for verification."
        super().__init__("Halal Validator Agent", system_prompt)

    def process_validation(self, recipes: List[Dict]) -> List[Dict]:
        """
        Validates ingredients using the Built-in Tool simulation.
        This is the other half of the Parallel Block.
        """
        validated_recipes = []
        
        for recipe in recipes:
            is_valid = True
            
            # Check suspicious ingredients
            for ingredient in recipe['ingredients']:
                if ingredient.lower() in ["gelatin", "lard", "pork derivatives"]:
                    # Demonstrates Built-in Tool usage
                    verification_result = google_search_halal_verifier(ingredient) 
                    
                    if "FAIL" in verification_result:
                        is_valid = False
                        # Demonstrates Observability (Logging rejection reason)
                        print(f"  [Validator] 🚨 LOG: REJECTED '{recipe['title']}' - Reason: {verification_result}")
                        break
            
            if is_valid:
                validated_recipes.append(recipe)
                
        return validated_recipes