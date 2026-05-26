class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        unique_chars = set(word)
        
        # Filter into lowercase and uppercase sets
        lowers = {c for c in unique_chars if c.islower()}
        uppers = {c.lower() for c in unique_chars if c.isupper()}
        
        # The length of the intersection gives the number of special letters
        return len(lowers & uppers)
    
#tarronnsaiadabala