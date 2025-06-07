class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n2 = nums2.size();
        int n1 = nums1.size();
        vector<int> hash(10005);
        for(int i=0; i<10005; i++)
            hash[i] = -1;
        stack<int> s;
        for(int i=0; i<n2; i++){
            while(!s.empty() && s.top()<nums2[i]){
                hash[s.top()] = nums2[i];
                s.pop();
            }
            s.push(nums2[i]);
        }
        for(int i=0; i<n1; i++){
            nums1[i] = hash[nums1[i]];
        }
        return nums1;
    }
};