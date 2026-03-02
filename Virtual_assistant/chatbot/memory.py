import json
import os
import time 


class ConversationMemory:
    """
    Intelligent memory system with confidence, priority, and decay.
    """

    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        self.memory = {}
        self._load_memory()

    # ---------- Persistence ----------
    def _load_memory(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.memory = json.load(file)

    def _save_memory(self):
        with open(self.file_path, "w") as file:
            json.dump(self.memory, file, indent=4)

    # ---------- Memory Intelligence ----------
    def remember(
        self,
        key: str,
        value: str,
        confidence: float = 1.0,
        priority: int = 3
    ):
        """
        Stores memory with intelligence metadata.
        """

        self.memory[key] = {
            "value": value,
            "confidence": confidence,
            "priority": priority,
            "timestamp": time.time()
        }
        # ⚠️ KEY LINE: Rich memory representation

        self._save_memory()

    def recall(self, key: str):
        """
        Returns memory value if strong enough.
        """
        item = self.memory.get(key)

        if not item:
            return None

        if item["confidence"] < 0.4:
            return None
            # ⚠️ KEY LINE: Weak memories are ignored

        return item["value"]

    def forget_low_priority(self, min_priority: int = 2):
        """
        Deletes unimportant memories.
        """
        self.memory = {
            k: v for k, v in self.memory.items()
            if v["priority"] >= min_priority
        }
        self._save_memory()

    def decays_memory(self, max_age_seconds: int = 86400):
        """
        Weakens memory confidence over time.
        """
        now = time.time()

        for item in self.memory.values():
            age = now - item["timestamp"]
            if age > max_age_seconds:
                item["confidence"] *= 0.5
                # ⚠️ KEY LINE: Memory decay

        self._save_memory()

    def has(self, key: str) -> bool:
        return key in self.memory
        
    
               
    
         
  
    
    

  


          

        
 



        
        
        

          

       


