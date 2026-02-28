import json
import os



class ConversationMemory:
    
    """
  Stores and manages conversation context.
  """
    
    def __init__(self, file_path="memory.json"):
        # Dictionary to store remembered facts
        self.file_path = file_path
        self.memory = {}
        
        self._load_memory()
        
    def _load_memory(self):
        
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.memory = json.load(file)
                
    def _save_memory(self):
        
        "Saves a memory to disk."
        
        with open (self.file_path, "w") as file:
            json.dump(self.memory, file, indent=4)
            
            # KEY LINE: Memory persistence
            
        
 
        
       
          # ⚠️ KEY LINE: Centralized state storage
          
    def remember(self, key:str, value: str):
        """
        Saves information to memory.
        """

        self.memory[key] = value
        self._save_memory()
        
        
    def recall(self, key: str):
        """
        Retrieves information from memory.
        """
        
        return self.memory.get(key)
    
    def has(self, key: str) -> bool:
        """
        Checks if a piece of memory exists.
        """
        
        return key in self.memory

        
    
         
  
    
    

  


          

        
 



        
        
        

          

       

