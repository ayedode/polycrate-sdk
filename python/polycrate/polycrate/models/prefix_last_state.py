from typing import Literal

PrefixLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PREFIX_LAST_STATE_VALUES: set[PrefixLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_prefix_last_state(value: str) -> PrefixLastState:
    if value in PREFIX_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_LAST_STATE_VALUES!r}")
