/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int goodNodes(TreeNode* root) {
        return recurse(root, INT_MIN);
    }

    int recurse(TreeNode* node, int max_node){
        if(!node) return 0;

        int val = recurse(node->left, max(max_node, node->val)) + recurse(node->right, max(max_node, node->val));

        if (node->val >= max_node) val+= 1;

        return val;
    }
};