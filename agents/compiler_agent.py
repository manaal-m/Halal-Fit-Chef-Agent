# agents/compiler_agent.py
from agents.agent_core import LLM_Agent_Core
# We need to import the class from the services folder
from services.memory_bank import MemoryBank 
from typing import List, Dict
import json

class PlanCompilerAgent(LLM_Agent_Core):
    def __init__(self, memory_bank: MemoryBank):
        system_prompt = "Compile validated recipes into a daily meal plan. Generate shopping list. Prioritize favorites from Memory Bank."
        super().__init__("Plan Compiler Agent", system_prompt)
        self.memory_bank = memory_bank

    def compile_plan(self, constraints: dict, validated_recipes: List[Dict]) -> dict:
        """
        Compiles the final plan, utilizing Long Term Memory.
        """
        
        # Demonstrates Long Term Memory usage
        favorites = self.memory_bank.retrieve_favorites(constraints.get("cuisine", "Indian"))
        print(f"  [Compiler] Retrieved favorites from Memory: {favorites}")
        
        # Simple scheduling logic
        plan = {
            "Day 1 (Priority)": validated_recipes[0]['title'] if validated_recipes else favorites[0] if favorites else "Vegetable Biryani",
            "Day 2": validated_recipes[0]['title'] if len(validated_recipes) > 1 else "High-Protein Lentil Curry",
            "Day 3": validated_recipes[0]['title'] if len(validated_recipes) > 2 else "Chicken Tikka (Halal)",
        }

        # Final Compilation
        final_plan = {
            "constraints": constraints,
            "schedule": plan,
            "recipes": validated_recipes,
            "shopping_list": ["Tofu 500g", "Indian Spices", "Chicken 1kg (Halal certified)"]
        }
        
        # Assume plan is successful and store it
        self.memory_bank.store_plan(final_plan, rating=5) 

        return final_plan