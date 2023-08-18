class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numset;

        for(auto num : nums) {
            numset.insert(num);
        }

        int low, num, maxrange = 0, range;


        while(!numset.empty()) {
            range = 0;

            num = *numset.begin();

            low = num; 

            while(numset.erase(low-1)) {
                low--;
                range++;
            }

            while(numset.erase(num)) {
                num++;
                range++;
            }

            maxrange = max(range, maxrange);
        }

        return maxrange;

        

    }
};