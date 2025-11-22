# services/session_service.py
from typing import Dict, Optional

class InMemorySessionService:
    """
    Implements Sessions & State Management (InMemorySessionService).
    Allows for pause/resume of the planning process (Long-running operations).
    """
    def __init__(self):
        self.session_data: Dict[str, dict] = {}
        print("[Service Init] Session Service initialized.")

    def save_state(self, session_id: str, data: dict):
        self.session_data[session_id] = data
        print(f"  [State] Session {session_id} state SAVED.")
    
    def load_state(self, session_id: str) -> Optional[dict]:
        state = self.session_data.get(session_id)
        if state:
            print(f"  [State] Session {session_id} state LOADED.")
        return state