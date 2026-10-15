from typing import Literal

PrefixState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PREFIX_STATE_VALUES: set[PrefixState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_prefix_state(value: str) -> PrefixState:
    if value in PREFIX_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_STATE_VALUES!r}")
