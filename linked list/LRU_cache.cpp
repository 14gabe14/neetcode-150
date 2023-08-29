class Node {
public:
    int key;
    int val;
    Node * next;
    Node * prev;

    Node(int _key, int _val) {
        key = _key;
        val = _val;
        next = nullptr;
        prev = nullptr;
    }
};

class LRUCache {
public:
    int capacity;
    int length;
    Node * head;
    Node * tail;
    unordered_map<int, Node*> nodeMap;

    LRUCache(int _capacity) {
        capacity = _capacity;
        head = nullptr;
        tail = nullptr;
    }
    
    int get(int key) {
        if(nodeMap.find(key) == nodeMap.end()) return -1;
        Node * node = nodeMap[key];
        moveToHead(node);
        return node->val;
    }
    
    void put(int key, int value) {
        Node * node;

        if (nodeMap.find(key) != nodeMap.end()) {
            node = nodeMap[key];
            moveToHead(node);
            node->val = value;
            return;
        }

        node = new Node(key, value);

        if (head) {
            head->prev = node;
            node->next = head;
            head = node;
        } else {
            head = node;
        }

        if (!tail) tail = node;

        nodeMap[key] = node;

        if (nodeMap.size() > capacity) {
            nodeMap.erase(tail->key);
            Node *prevTail = tail;
            tail = tail->prev;
            if(tail) tail->next = nullptr;
            delete prevTail;
        }

    }
    
    void moveToHead(Node* node) {
        if(node == head) return;
        if(node == tail) {
            tail = node->prev;
            tail->next = nullptr;
        } else {
            node->prev->next = node->next;
            node->next->prev = node->prev;
        }

        node->next = head;
        head->prev = node;
        node->prev = nullptr;
        head = node;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */