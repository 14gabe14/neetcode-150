const int ALPHABET_LEN = 26;

struct TrieNode {
    struct TrieNode * children[ALPHABET_LEN] = {nullptr};
    bool end = false;
};

class WordDictionary {
public:
    struct TrieNode * root;

    WordDictionary() {
        root = new TrieNode;
    }
    
    void addWord(string word) {
        struct TrieNode * current = root;
        int index;

        for(char c: word) {
            index = c-'a';
            if (current->children[index] == nullptr) {
                current->children[index] = new TrieNode();
            }
                current = current->children[index];
        }

        current->end = true;
    }
    
    bool search(string word) {
        if (root!=nullptr) return recurse(root, word, 0);
        return false;
    }

    bool recurse(TrieNode * node, string word, int char_index) {
        if (char_index == word.size()) {
            return node->end;
        }

        if(word[char_index] == '.') {
            for (int i = 0; i < ALPHABET_LEN; i++) {
                if (node->children[i] != nullptr && recurse(node->children[i], word, char_index+1)) return true;
            }
            return false;
        }
        
        if(node->children[word[char_index]-'a'] != nullptr) {
            return recurse(node->children[word[char_index]-'a'], word, char_index+1);
        }
        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */