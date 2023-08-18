class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> nummap;

        for(int i = 0; i < numbers.size(); i++) {
            if(nummap.count(numbers[i]) > 0) {
                return {nummap[numbers[i]]+1, i+1};
            } else {
                nummap[target-numbers[i]] = i;
            }
        }

        return {};
    }
};