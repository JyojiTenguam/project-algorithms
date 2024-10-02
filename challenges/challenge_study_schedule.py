def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    count = 0

    for period in permanence_period:
        if not (isinstance(period, tuple) and len(period) == 2 and
                isinstance(period[0], int) and isinstance(period[1], int)):
            return None
        entry, exit = period
        if entry <= target_time <= exit:
            count += 1

    return count
