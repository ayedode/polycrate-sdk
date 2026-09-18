from typing import Literal

OutcomeEnum = Literal["denied", "error", "ok"]

OUTCOME_ENUM_VALUES: set[OutcomeEnum] = {
    "denied",
    "error",
    "ok",
}


def check_outcome_enum(value: str) -> OutcomeEnum:
    if value in OUTCOME_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OUTCOME_ENUM_VALUES!r}")
