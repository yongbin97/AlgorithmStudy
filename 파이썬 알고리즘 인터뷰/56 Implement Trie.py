class Trie2:
    def __init__(self):
        self.trie_dict = {}

    def insert(self, word: str) -> None:
        idx = 0
        word_dict = self.trie_dict

        while idx < len(word):
            if word[idx] not in word_dict:
                word_dict[word[idx]] = {}
            word_dict = word_dict[word[idx]]

            if idx == len(word) - 1:
                word_dict["is_word"] = True
            idx += 1

    def search(self, word: str) -> bool:
        idx = 0
        word_dict = self.trie_dict
        while idx < len(word):
            if word[idx] not in word_dict:
                return False
            word_dict = word_dict[word[idx]]
            idx += 1
        return word_dict.get("is_word", False)

    def startsWith(self, prefix: str) -> bool:
        idx = 0
        word_dict = self.trie_dict
        while idx < len(prefix):
            if prefix[idx] not in word_dict:
                return False
            word_dict = word_dict[prefix[idx]]
            idx += 1
        return True



class TrieNode:
    def __init__(self):
        self.word = False
        self.child = {}

class Trie:

    def __init__(self):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self._root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# Your Trie object will be instantiated and called as such:
word = "apple"
word2 = "abcde"
obj = Trie()
obj.insert(word)
obj.insert(word2)
param_2 = obj.search(word)
param_3 = obj.startsWith("app")

print(param_2, param_3)