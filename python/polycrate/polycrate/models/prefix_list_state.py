from typing import Literal

PrefixListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PREFIX_LIST_STATE_VALUES: set[PrefixListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_prefix_list_state(value: str) -> PrefixListState:
    if value in PREFIX_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_LIST_STATE_VALUES!r}")
