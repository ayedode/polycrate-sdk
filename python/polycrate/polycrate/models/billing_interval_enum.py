from typing import Literal

BillingIntervalEnum = Literal["day", "hour", "minute", "month", "second", "year"]

BILLING_INTERVAL_ENUM_VALUES: set[BillingIntervalEnum] = {
    "day",
    "hour",
    "minute",
    "month",
    "second",
    "year",
}


def check_billing_interval_enum(value: str) -> BillingIntervalEnum:
    if value in BILLING_INTERVAL_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLING_INTERVAL_ENUM_VALUES!r}")
