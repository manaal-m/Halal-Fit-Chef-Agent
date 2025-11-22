# agents/generator_agent.py
from agents.agent_core import LLM_Agent_Core
# We need to import the Custom Tool
from tools.nutritional_macros import calculate_nutritional_macros
from typing import List, Dict

class RecipeGeneratorAgent(LLM_Agent_Core):
    def __init__(self):
        system_prompt = "Generate recipes matching nutritional goals (high-protein, low-carb) and Indian cuisine."
        super().__init__("Recipe Generator Agent", system_prompt)

    def process_generation(self, constraints: dict) -> List[Dict]:
        """
        Generates recipes and calls the Custom Tool for nutritional verification.
        This is one half of the Parallel Block.
        """
        # Placeholder Generation: Note one recipe contains 'Gelatin' and one contains 'Lard' for the Validator Agent to reject
        recipes_to_check = [
            {"title": "High-Protein Tofu Tikka Masala", "ingredients": ["Tofu", "Yogurt", "Spices"]},
            {"title": "Kheer with Gelatin Stabilizer", "ingredients": ["Rice", "Milk", "Gelatin"]},
            {"title": "Chicken Seekh Kebab", "ingredients": ["Chicken", "Spices", "Lard"]}
        ]

        for recipe in recipes_to_check:
            # Demonstrates Custom Tool usage
            ingredients_list = recipe["ingredients"] 
            macros = calculate_nutritional_macros(ingredients_list)
            recipe["macros"] = macros
            print(f"  [Generator] Proposed '{recipe['title']}' | Protein: {macros['protein_g']}g")

        return recipes_to_check