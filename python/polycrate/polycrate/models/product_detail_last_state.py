from typing import Literal

ProductDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRODUCT_DETAIL_LAST_STATE_VALUES: set[ProductDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_product_detail_last_state(value: str) -> ProductDetailLastState:
    if value in PRODUCT_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_LAST_STATE_VALUES!r}")
