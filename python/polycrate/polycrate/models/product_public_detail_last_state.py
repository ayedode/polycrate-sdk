from typing import Literal

ProductPublicDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRODUCT_PUBLIC_DETAIL_LAST_STATE_VALUES: set[ProductPublicDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_product_public_detail_last_state(value: str) -> ProductPublicDetailLastState:
    if value in PRODUCT_PUBLIC_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_DETAIL_LAST_STATE_VALUES!r}")
