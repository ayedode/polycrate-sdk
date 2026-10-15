from typing import Literal

ProductPublicListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRODUCT_PUBLIC_LIST_STATE_VALUES: set[ProductPublicListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_product_public_list_state(value: str) -> ProductPublicListState:
    if value in PRODUCT_PUBLIC_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_LIST_STATE_VALUES!r}")
