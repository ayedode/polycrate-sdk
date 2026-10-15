from typing import Literal

ProductSimpleBillingInterval = Literal["day", "hour", "minute", "month", "second", "year"]

PRODUCT_SIMPLE_BILLING_INTERVAL_VALUES: set[ProductSimpleBillingInterval] = {
    "day",
    "hour",
    "minute",
    "month",
    "second",
    "year",
}


def check_product_simple_billing_interval(value: str) -> ProductSimpleBillingInterval:
    if value in PRODUCT_SIMPLE_BILLING_INTERVAL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_SIMPLE_BILLING_INTERVAL_VALUES!r}")
