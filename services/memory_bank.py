# services/memory_bank.py
from collections import deque
from typing import Dict, List

class MemoryBank:
    """
    Implements Long Term Memory (Memory Bank) for learned preferences.
    """
    def __init__(self):
        # Stores past successful, high-rated plans (fixed size)
        self.successful_plans: deque = deque(maxlen=10)
        print("[Service Init] Memory Bank initialized.")

    def store_plan(self, plan: dict, rating: int):
        if rating >= 4:
            self.successful_plans.appendleft(plan)
            print(f"  [Memory] Plan stored in Memory Bank (Rating: {rating}).")
            
    def retrieve_favorites(self, cuisine: str) -> List[str]:
        """Retrieves titles of successful recipes based on cuisine."""
        favorites = []
        for plan in self.successful_plans:
            # Assuming 'recipes' key exists
            recipe_titles = [r['title'] for r in plan.get('recipes', [])]
            favorites.extend(recipe_titles)
        return list(set(favorites)) # Return unique titles