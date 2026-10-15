from typing import Literal

ProductDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRODUCT_DETAIL_STATE_VALUES: set[ProductDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_product_detail_state(value: str) -> ProductDetailState:
    if value in PRODUCT_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_STATE_VALUES!r}")
