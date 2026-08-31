from typing import Literal

BudgetedHoursModeEnum = Literal["retainer", "tm"]

BUDGETED_HOURS_MODE_ENUM_VALUES: set[BudgetedHoursModeEnum] = {
    "retainer",
    "tm",
}


def check_budgeted_hours_mode_enum(value: str) -> BudgetedHoursModeEnum:
    if value in BUDGETED_HOURS_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUDGETED_HOURS_MODE_ENUM_VALUES!r}")
