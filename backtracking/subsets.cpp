class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> answer;
        vector<int> temp;

        backtrack(answer, temp, nums, 0);
        return answer;
    }

    void backtrack(vector<vector<int>>& answer, vector<int>& temp, vector<int>& nums, int start) {
        answer.push_back(temp);

        for(int i = start; i < nums.size(); i++) {
            temp.push_back(nums[i]);
            backtrack(answer, temp, nums, i + 1);
            temp.pop_back();
        }
    }
};