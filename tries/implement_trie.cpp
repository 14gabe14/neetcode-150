const int ALPHABET_LEN = 26;

struct TrieNode {
    struct TrieNode * children[ALPHABET_LEN] = {nullptr};
    bool end = false;
};

class Trie {
public:
    TrieNode * root;

    Trie() {
        root = new TrieNode;
    }
    
    void insert(string word) {
        struct TrieNode * current = root;
        int index;

        for(char c: word) {
            index = c-'a';
            if (current->children[index] == nullptr) {
                current->children[index] = new TrieNode;
            }
                current = current->children[index];
        }

        current->end = true;
    }
    
    bool search(string word) {
        struct TrieNode * current = root;
        
        for(char c: word) {
            if (current == nullptr) return false;

            current = current->children[c-'a'];
        }

        if (current != nullptr && current->end) {
            return true;
        }

        return false;
    }
    
    bool startsWith(string prefix) {
        struct TrieNode * current = root;

        for(char c: prefix) {
            if (current == nullptr) return false;

            current = current->children[c-'a'];
        }

        if (current != nullptr) {
            return true;
        }
        
        return false;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */