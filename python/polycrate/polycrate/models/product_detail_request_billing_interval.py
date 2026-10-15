from typing import Literal

ProductDetailRequestBillingInterval = Literal["day", "hour", "minute", "month", "second", "year"]

PRODUCT_DETAIL_REQUEST_BILLING_INTERVAL_VALUES: set[ProductDetailRequestBillingInterval] = {
    "day",
    "hour",
    "minute",
    "month",
    "second",
    "year",
}


def check_product_detail_request_billing_interval(value: str) -> ProductDetailRequestBillingInterval:
    if value in PRODUCT_DETAIL_REQUEST_BILLING_INTERVAL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_REQUEST_BILLING_INTERVAL_VALUES!r}")
