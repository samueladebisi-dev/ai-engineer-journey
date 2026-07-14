def average(values: list[float]) -> float:
    if not values:
        return 0

    return sum(values) / len(values)

def maximum(values: list[float]) -> float:
    return max(values) if values else 0

def minimum(values: list[float]) -> float:
    return min(values) if values else 0

def total(values: list[float]) -> float:
    return sum(values)