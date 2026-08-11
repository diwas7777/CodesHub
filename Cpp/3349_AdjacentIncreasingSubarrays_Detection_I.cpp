#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;


class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int inc = 1;
        int prevInc = 0;
        int maxLen = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                inc++;
            } else {
                prevInc = inc;
                inc = 1;
            }
            maxLen = max(maxLen, max(inc >> 1, min(prevInc, inc)));
            if (maxLen >= k) return true;
        }
        return false;
    }
};


int main() {
    Solution sol;
    vector<int> nums;
    int n, k;
    cout << "Enter n (size), k: ";
    cin >> n >> k;
    nums.resize(n);
    cout << "Enter array elements: ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    bool res = sol.hasIncreasingSubarrays(nums, k);
    if (res)
        cout << "Yes, there is a subarray satisfying the condition.\n";
    else
        cout << "No such subarray exists.\n";
    return 0;
}
