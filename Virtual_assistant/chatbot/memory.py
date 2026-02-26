class ConversationMemory:
    
    """
  Stores and manages conversation context.
  """
    
    def __init__(self):
          # Dictionary to store remembered facts
          self.memory = {}
          # ⚠️ KEY LINE: Centralized state storage
    def remember(seld, key:str, value: str):
        """
        Saves information to memory.
        """

        seld.memory[key] = value
        
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

        

    
         
  
    
    

  


          

        
 



        
        
        

          

       
