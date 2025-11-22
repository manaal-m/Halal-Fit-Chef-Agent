# tools/nutritional_macros.py
from typing import List, Dict

def calculate_nutritional_macros(recipe_ingredients: List[str]) -> Dict[str, float]:
    """
    Custom Tool: Calculates estimated Calories, Protein, and Carbs per serving.
    Demonstrates Custom Tool application.
    """
    protein = 100.0
    carbs = 0.0
    
    # Simplified placeholder logic based on ingredient types
    if any(i.lower() in recipe_ingredients for i in ["chicken", "paneer", "tofu"]):
        protein += 25.0
    if any(i.lower() in recipe_ingredients for i in ["rice", "potato", "maida"]):
        carbs += 40.0
        
    estimated_calories = (protein * 4) + (carbs * 4) + 150 # Add some fat/other calories
    
    return {
        "calories": round(estimated_calories, 1),
        "protein_g": round(protein, 1),
        "carbs_g": round(carbs, 1)
    }