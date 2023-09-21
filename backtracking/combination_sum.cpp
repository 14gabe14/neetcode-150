class Solution {
public:
    int _target;
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        _target = target;
        vector<vector<int>> result;
        vector<int> temp;

        backtrack(result, temp, candidates, 0, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& temp, vector<int>& candidates, int start, int sum) {
        if (sum == _target) {
            result.push_back(temp);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if(sum < _target) {
                temp.push_back(candidates[i]);           
                backtrack(result, temp, candidates, i, sum + candidates[i]);
                temp.pop_back();    
            }
        }
    }
};