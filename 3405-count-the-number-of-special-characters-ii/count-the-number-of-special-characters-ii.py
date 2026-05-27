class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Dictionaries to store the last lowercase and first uppercase indices
        last_lowercase = {}
        first_uppercase = {}
        
        # Iterate through the string to map out the positions
        for idx, char in enumerate(word):
            if char.islower():
                # Always update to get the LAST occurrence
                last_lowercase[char] = idx
            elif char.isupper():
                # Only record the FIRST occurrence
                if char not in first_uppercase:
                    first_uppercase[char] = idx
                    
        special_count = 0
        
        # Check all unique lowercase letters found
        for char in last_lowercase:
            upper_char = char.upper()
            
            # Condition: Must exist in uppercase, and last lowercase < first uppercase
            if upper_char in first_uppercase:
                if last_lowercase[char] < first_uppercase[upper_char]:
                    special_count += 1
                    
        return special_count

#tarronnsaiadabala