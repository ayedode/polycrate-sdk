from typing import Literal

OrganizationProductListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ORGANIZATION_PRODUCT_LIST_STATE_VALUES: set[OrganizationProductListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_organization_product_list_state(value: str) -> OrganizationProductListState:
    if value in ORGANIZATION_PRODUCT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_LIST_STATE_VALUES!r}")
