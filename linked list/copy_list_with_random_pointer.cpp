/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        unordered_map<Node*, Node*> nodeMap;
        Node * current = head;
        Node * current_copy;

        while (current) {
            current_copy = new Node(current->val);
            nodeMap[current] = current_copy;
            current = current->next;
        }

        current = head;
        current_copy = nodeMap[head];

        while (current) {
            current_copy->next = nodeMap[current->next];
            current_copy->random = nodeMap[current->random];
            current = current->next;
            current_copy =current_copy->next;
        }

        return nodeMap[head];

        
    }
};