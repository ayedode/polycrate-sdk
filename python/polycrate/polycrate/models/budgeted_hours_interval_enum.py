from typing import Literal

BudgetedHoursIntervalEnum = Literal["day", "hour", "minute", "month", "project", "second", "year"]

BUDGETED_HOURS_INTERVAL_ENUM_VALUES: set[BudgetedHoursIntervalEnum] = {
    "day",
    "hour",
    "minute",
    "month",
    "project",
    "second",
    "year",
}


def check_budgeted_hours_interval_enum(value: str) -> BudgetedHoursIntervalEnum:
    if value in BUDGETED_HOURS_INTERVAL_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUDGETED_HOURS_INTERVAL_ENUM_VALUES!r}")
