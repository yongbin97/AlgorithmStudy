class TrieNode {
    boolean word;
    TrieNode[] children;

    public TrieNode() {
        this.word = false;
        this.children = new TrieNode[26];
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = this.root;

        for (char c: word.toCharArray()){
            if (node.children[c - 'a'] == null) {
                node.children[c - 'a'] = new TrieNode();
            }
            node = node.children[c - 'a'];
        }
        node.word = true;
    }
    
    public boolean search(String word) {
        TrieNode node = this.root;

        for (char c: word.toCharArray()){
            if (node.children[c - 'a'] != null){
                node = node.children[c - 'a'];
            }
            else return false;
        }
        return node.word;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = this.root;

        for (char c: prefix.toCharArray()){
            if (node.children[c - 'a'] != null){
                node = node.children[c - 'a'];
            }
            else return false;
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */