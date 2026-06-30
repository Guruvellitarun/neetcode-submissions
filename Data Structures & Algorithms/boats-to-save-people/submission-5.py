class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        no_of_boats = 0
        l = 0
        r = len(people)-1

        while l <= r:
            weight = people[l] + people[r]
            if weight <= limit:
                l += 1 
            r -= 1
            no_of_boats += 1

        return no_of_boats