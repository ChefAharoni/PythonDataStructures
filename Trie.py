class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary mapping char to TrieNode
        self.is_end_of_word = False  # True if node represents end of word


class Trie:
    """
    A class used to represent a Trie (prefix tree).
    Attributes
    ----------
    root : TrieNode
        The root node of the Trie.
    Methods
    -------
    __init__():
        Initializes the Trie with a root node.
    insert(word):
        Inserts a word into the Trie.
    search(word):
        Searches for a word in the Trie.
    starts_with(prefix):
        Checks if there is any word in the Trie that starts with the given prefix.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to be inserted into the Trie.

        Returns:
            None
        """
        current = self.root
        for char in word:
            # If character not present, add a new node
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True  # Mark the end of a word

    def search(self, word):
        """
        Searches for a word in the Trie.
        Args:
            word (str): The word to search for in the Trie.
        Returns:
            bool: True if the word exists in the Trie and is marked as a complete word, False otherwise.
        """

        current = self.root
        for char in word:
            # If character not present, word doesn't exist
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word  # True if it's end of a valid word

    def starts_with(self, prefix):
        """
        Checks if there is any word in the trie that starts with the given prefix.
        Args:
            prefix (str): The prefix to check in the trie.
        Returns:
            bool: True if there is any word in the trie that starts with the given prefix, False otherwise.
        """

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
