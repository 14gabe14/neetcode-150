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
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        vector<vector<int>> result;
        vector<int> level;
        
        if (root == NULL) return result;
        
        vector<TreeNode*> nodes;
        vector<TreeNode*> children;
        
        nodes.push_back(root);
        
        while (nodes.size() != 0) {
            
            for (TreeNode* parent : nodes) {
                level.push_back(parent->val);
                if (parent->left) children.push_back(parent->left);
                if (parent->right) children.push_back(parent->right);
            }

            nodes = children;
            children.clear();
            
            result.push_back(level);
            level.clear();
        }
        
        return result;
        
        
    }
};