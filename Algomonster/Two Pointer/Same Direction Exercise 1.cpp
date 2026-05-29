// LeetCode 26. Remove Duplicates from Sorted Array
// http://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

int remove_duplicates(std::vector<int>& arr) {
    int slow = 0;
    for (int fast = 0; fast < (int)arr.size(); fast++) {
        if (arr[fast] != arr[slow]) {
            slow++;
            arr[slow] = arr[fast];
        }
    }
    return slow + 1;
}

/* Explanation

*/