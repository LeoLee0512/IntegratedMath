"""Exact recurrence from chapter 1; no floating-point approximation."""
import json


def simulate(steps=3):
    if not isinstance(steps, int) or isinstance(steps, bool) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    volume = 5
    records = [{"minute": 0, "volume_litres": volume}]
    for minute in range(1, steps + 1):
        volume = volume + 2
        records.append({"minute": minute, "volume_litres": volume})
    return records


if __name__ == "__main__":
    print(json.dumps(simulate(), ensure_ascii=False, indent=2))
