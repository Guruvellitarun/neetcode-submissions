class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l, r = 0, len(people)-1
        boat = 0
        while r >= l:
            if people[r] + people[l] <= limit:
                l += 1
            boat += 1
            r -= 1
        return boat
