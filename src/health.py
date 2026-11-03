"""Synthetic load classifier for Night Watch Demo."""


def classify_load(percent: int) -> str:
    """Return OK for normal load and DEGRADED for high load.

    Args:
        percent: Integer load percentage from 0 through 100.
    """
    if not isinstance(percent, int) or not 0 <= percent <= 100:
        raise ValueError("percent must be an integer from 0 to 100")
    if percent < 80:
        return "OK"
    return "DEGRADED"
