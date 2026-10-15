from typing import Literal

PopOwnRz = Literal["no", "planned", "unknown", "yes"]

POP_OWN_RZ_VALUES: set[PopOwnRz] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_own_rz(value: str) -> PopOwnRz:
    if value in POP_OWN_RZ_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_OWN_RZ_VALUES!r}")
