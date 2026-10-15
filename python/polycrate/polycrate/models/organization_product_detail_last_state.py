from typing import Literal

OrganizationProductDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ORGANIZATION_PRODUCT_DETAIL_LAST_STATE_VALUES: set[OrganizationProductDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_organization_product_detail_last_state(value: str) -> OrganizationProductDetailLastState:
    if value in ORGANIZATION_PRODUCT_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_LAST_STATE_VALUES!r}")
