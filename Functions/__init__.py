def computeNewChance(originalChance, newChance) -> float:
    return min(1 - ((1 - originalChance) * (1 - newChance)), 1)