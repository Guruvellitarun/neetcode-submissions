class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        no_of_boats = 0
        l = 0
        r = len(people)-1

        while l <= r:
            if people[r] >= limit:
                r -= 1
                no_of_boats += 1
                continue

            # if l == r:
            #     no_of_boats += 1
            weight = people[l] + people[r]
            if weight > limit:
                r -= 1
                no_of_boats += 1
            elif weight < limit:
                l += 1
                r -= 1
                no_of_boats += 1
            elif weight == limit:
                no_of_boats += 1
                l += 1
                r -= 1
        return no_of_boats