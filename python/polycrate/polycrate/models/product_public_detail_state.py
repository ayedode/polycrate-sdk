from typing import Literal

ProductPublicDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRODUCT_PUBLIC_DETAIL_STATE_VALUES: set[ProductPublicDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_product_public_detail_state(value: str) -> ProductPublicDetailState:
    if value in PRODUCT_PUBLIC_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_DETAIL_STATE_VALUES!r}")
