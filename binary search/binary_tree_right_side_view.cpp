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
    vector<int> view;

    vector<int> rightSideView(TreeNode* root) {
        traverse(root, 1);

        return view;
    }

    void traverse(TreeNode* root, int depth) {
        if(root){
            if(depth > view.size()) {
                view.push_back(root->val);
            }

            traverse(root->right, depth+1);
            traverse(root->left, depth+1);
        }
    }
};