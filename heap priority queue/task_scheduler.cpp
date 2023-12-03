class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        if (n == 0) return tasks.size();

        unordered_map<char, int> taskcount;

        for(char c : tasks) {
            if(taskcount.count(c) > 0) {
                taskcount[c]++;
            } else {
                taskcount[c] = 1;
            }
        }

        priority_queue<int> nodes;
        queue<int> popped;
        int j = 0;

        for (auto n: taskcount) {
            nodes.push(n.second);
        }

        while(!nodes.empty()) {

            for(int i = 0; i < n+1; i++) {
                if(nodes.empty()) {
                    if(popped.empty()) {
                        break;
                    } else {
                        j++;
                        continue;
                    }
                } 
                if(nodes.top()>1) popped.push(nodes.top()-1);
                nodes.pop();
                j++;
            }

            while(!popped.empty()) {
                nodes.push(popped.front());
                popped.pop();
            }
        }
        
        return j;
    }
};