class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        unordered_map<int,int> mp;
        for(int ele : target)
            mp[ele]++;
        for(int ele : arr)
            mp[ele]--;
        for(auto pairs : mp)
            if(pairs.second)
                return false;
        return true;
    }
};
