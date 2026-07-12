def average(values: list[float]) -> float:
    if not values:
        return 0

    return sum(values) / len(values)

def maximum(values: list[float]) -> float:
    return max(values) if values else 0