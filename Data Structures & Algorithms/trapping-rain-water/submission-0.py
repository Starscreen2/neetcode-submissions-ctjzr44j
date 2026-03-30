class Solution:
    def trap(self, height: List[int]) -> int:
        # from each index of the array we place a water block, and then expand left and right
        # for literal edge, the water would flow off, so no go, we move on to the next index. 
        # we expand until both the left and the right hits a wall, then we add those blocks to temp
        # we go up, and repeat expanding to the left and to the right, until both sides hits a wall
        # if there is a block in the way, then no

        if not height:
            return 0

        max_h = max(height)
        water = 0

        # Fill level by level (like stacking water blocks upward)
        for lvl in range(1, max_h + 1):
            seen_left_wall = False
            gap = 0  # potential water blocks at this level between walls

            for h in height:
                if h >= lvl:
                    # We hit a wall at this level.
                    # If we already saw a left wall, the gap becomes trapped water.
                    if seen_left_wall:
                        water += gap
                    # Reset gap, keep walls going
                    seen_left_wall = True
                    gap = 0
                else:
                    # This is an empty spot at this level.
                    # Only counts if we've already seen a left wall (otherwise it leaks off the left edge).
                    if seen_left_wall:
                        gap += 1

        return water