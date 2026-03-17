def make_bricks(small, big, goal):
    max_big_used = min(big, goal // 5)
    remainder = goal - max_big_used * 5
    return remainder <= small