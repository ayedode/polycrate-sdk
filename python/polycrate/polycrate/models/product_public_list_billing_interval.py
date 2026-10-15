from typing import Literal

ProductPublicListBillingInterval = Literal["day", "hour", "minute", "month", "second", "year"]

PRODUCT_PUBLIC_LIST_BILLING_INTERVAL_VALUES: set[ProductPublicListBillingInterval] = {
    "day",
    "hour",
    "minute",
    "month",
    "second",
    "year",
}


def check_product_public_list_billing_interval(value: str) -> ProductPublicListBillingInterval:
    if value in PRODUCT_PUBLIC_LIST_BILLING_INTERVAL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_LIST_BILLING_INTERVAL_VALUES!r}")
