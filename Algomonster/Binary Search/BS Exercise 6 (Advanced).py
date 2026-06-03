# LeetCode 1723. Find Minimum Time to Finish All Jobs
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/description/
# the soluton given in Algomonster doesnt work in Leetcode
# because in Leetcode problem, taking out order does not matter

# Wasnt able to solve. Summarized the answer

def feasible(newspapers_read_times: list[int], num_coworkers: int, limit: int) -> bool:
    # time to keep track of the current worker's time spent, num_workers to keep track of the number of coworkers used
    time, num_workers = 0, 0
    for read_time in newspapers_read_times:
        # check if current time exceeds the given time limit
        if time + read_time > limit:
            time = 0
            num_workers += 1
        time += read_time
    # edge case to check if we needed an extra worker at the end
    if time != 0:
        num_workers += 1
    # check if the number of workers we need is more than what we have
    return num_workers <= num_coworkers

def newspapers_split(newspapers_read_times: list[int], num_coworkers: int) -> int:
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        # helper function to check if a time works
        if feasible(newspapers_read_times, num_coworkers, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

""" 
Answer Summary

Key Insight
Goal is minimum time where all newspapers can be distributed, so we should ask:
[Given a time limit T, can we distribute all newspapers so no worker exceeds T minutes?]
Therefore, we should search for possible time limits, not distribution patterns

Search Bound
min possible time = longest single newspaper (one worker must read it)
max possible time = sum of all newspapers (one worker reads everything)

Feasibility Check
Start with first worker and running total of zero.
For each newspaper:
- if adding it keeps the total the same or under the limit, assign it to current worker
- otherwise, move to the next worker and assign newspaper to them

After processing all newspaper, count how many workers we used.
If the worker count exceeds, the time limit is too tight.
Otherwise, it works.

Complexity
Time: O(n log m)
Space: O(1)
"""

"""
Notes
In short, it repetitively check if the mid position is working.
mid position would work if we stack up the read time per worker.
"""