class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() == 1) return true;

        int maxjump = nums[0];
        int currentjump = nums[0];

        for(int i = 1; i < nums.size(); i++) {
            if (maxjump < i || maxjump + 1 >= nums.size()) {
                break;
            }

            currentjump = i + nums[i];
            maxjump = max(maxjump, currentjump);

        }

        return (maxjump + 1 >= nums.size());
    }
};