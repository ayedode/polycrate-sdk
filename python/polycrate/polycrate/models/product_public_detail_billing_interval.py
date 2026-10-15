from typing import Literal

ProductPublicDetailBillingInterval = Literal["day", "hour", "minute", "month", "second", "year"]

PRODUCT_PUBLIC_DETAIL_BILLING_INTERVAL_VALUES: set[ProductPublicDetailBillingInterval] = {
    "day",
    "hour",
    "minute",
    "month",
    "second",
    "year",
}


def check_product_public_detail_billing_interval(value: str) -> ProductPublicDetailBillingInterval:
    if value in PRODUCT_PUBLIC_DETAIL_BILLING_INTERVAL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_DETAIL_BILLING_INTERVAL_VALUES!r}")
