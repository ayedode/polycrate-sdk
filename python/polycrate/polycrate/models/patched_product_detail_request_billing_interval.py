from typing import Literal

PatchedProductDetailRequestBillingInterval = Literal["day", "hour", "minute", "month", "second", "year"]

PATCHED_PRODUCT_DETAIL_REQUEST_BILLING_INTERVAL_VALUES: set[PatchedProductDetailRequestBillingInterval] = {
    "day",
    "hour",
    "minute",
    "month",
    "second",
    "year",
}


def check_patched_product_detail_request_billing_interval(value: str) -> PatchedProductDetailRequestBillingInterval:
    if value in PATCHED_PRODUCT_DETAIL_REQUEST_BILLING_INTERVAL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRODUCT_DETAIL_REQUEST_BILLING_INTERVAL_VALUES!r}"
    )
