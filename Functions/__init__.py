def computeNewChance(originalChance, newChance) -> float:
    """
    Given two percentage chances for an event returns chance of the event occurring
    :param originalChance: Chance of event happening originally
    :param newChance: New chance of event occurring
    :return: Chance of event occurring
    """
    return min(1.0 - ((1.0 - originalChance) * (1.0 - newChance)), 1.0)