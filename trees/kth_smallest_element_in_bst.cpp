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
    int order;

    int kthSmallest(TreeNode* root, int k) {
        order = 0;
        return traverse(root, k);
    }

    int traverse(TreeNode* node, int k) {
        int val;
        if (node == nullptr) return -1;
        if ((val = traverse(node->left, k)) > -1) return val;
        if (++order == k) return node->val;
        if ((val = traverse(node->right, k)) > -1) return val;
        return -1;
    }
};