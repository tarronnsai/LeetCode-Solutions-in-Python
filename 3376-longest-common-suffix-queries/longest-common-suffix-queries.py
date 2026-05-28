class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the index of the best matching word for the suffix up to this node
        self.best_index = -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        # Helper to check if a new word index is better than the current best index
        def is_better(new_idx, curr_idx):
            if curr_idx == -1:
                return True
            if len(wordsContainer[new_idx]) < len(wordsContainer[curr_idx]):
                return True
            if len(wordsContainer[new_idx]) == len(wordsContainer[curr_idx]):
                return new_idx < curr_idx
            return False

        # Find the global default best index for words with NO common suffix
        # (This corresponds to the best word choice at the root node)
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if is_better(i, global_best_idx):
                global_best_idx = i
        
        root.best_index = global_best_idx
        
        # Build the Trie with reversed words
        for i, word in enumerate(wordsContainer):
            curr = root
            # Traverse backwards to handle suffixes as prefixes
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                # Update the node's best index if the current word is a better choice
                if is_better(i, curr.best_index):
                    curr.best_index = i
                    
        # Process queries
        ans = []
        for query in wordsQuery:
            curr = root
            # Traverse the Trie using the reversed query
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break # No longer matching common suffix
            
            # The best_index at the deepest matched node is our answer
            ans.append(curr.best_index)
            
        return ans

#tarronnsaiadabala