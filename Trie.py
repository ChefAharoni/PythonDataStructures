class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary mapping char to TrieNode
        self.is_end_of_word = False  # True if node represents end of word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            # If character not present, add a new node
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True  # Mark the end of a word

    def search(self, word):
        current = self.root
        for char in word:
            # If character not present, word doesn't exist
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word  # True if it's end of a valid word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True  # Prefix exists in trie


# Example usage:
trie = Trie()
trie.insert("hello")
trie.insert("helium")
print(trie.search("hello"))  # Output: True
print(trie.search("helix"))  # Output: False
print(trie.starts_with("he"))  # Output: True
print(trie.starts_with("hi"))  # Output: False
