def computeNewChance(originalChance, newChance) -> float:
    return min(1.0 - ((1.0 - originalChance) * (1.0 - newChance)), 1.0)