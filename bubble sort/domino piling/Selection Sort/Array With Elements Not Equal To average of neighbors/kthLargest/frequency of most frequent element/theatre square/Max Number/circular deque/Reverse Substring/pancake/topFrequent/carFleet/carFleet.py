def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    prev = None
    n = 0

    for pos, vel in sorted(zip(position, speed))[::-1]:
        distance = target - pos
        t = distance / vel

        if not prev or t > prev:
            prev = t
            n += 1

    return n
