from typing import Literal

ProductDetailBillingInterval = Literal["day", "hour", "minute", "month", "second", "year"]

PRODUCT_DETAIL_BILLING_INTERVAL_VALUES: set[ProductDetailBillingInterval] = {
    "day",
    "hour",
    "minute",
    "month",
    "second",
    "year",
}


def check_product_detail_billing_interval(value: str) -> ProductDetailBillingInterval:
    if value in PRODUCT_DETAIL_BILLING_INTERVAL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_BILLING_INTERVAL_VALUES!r}")
