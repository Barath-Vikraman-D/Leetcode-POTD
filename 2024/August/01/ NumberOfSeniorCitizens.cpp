//Solution in o(n) time complexity and O(1) space complexity

class Solution {
public:
    int countSeniors(vector<string>& details) {
        int seniorcount = 0,len=details.size(),age;
        for(int index=0;index<len;index++){
                age = (details[index][11]-'0')*10+details[index][12]-'0';//constructing number from string
                seniorcount+=(age>60); // checking whether the age is strictly greater than 60 or not
        }
        return seniorcount;
    }
};
