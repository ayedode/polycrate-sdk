from typing import Literal

OrganizationProductDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ORGANIZATION_PRODUCT_DETAIL_STATE_VALUES: set[OrganizationProductDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_organization_product_detail_state(value: str) -> OrganizationProductDetailState:
    if value in ORGANIZATION_PRODUCT_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_STATE_VALUES!r}")
