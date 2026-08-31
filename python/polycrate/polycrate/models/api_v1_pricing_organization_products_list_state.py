from typing import Literal

ApiV1PricingOrganizationProductsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_VALUES: set[ApiV1PricingOrganizationProductsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pricing_organization_products_list_state(value: str) -> ApiV1PricingOrganizationProductsListState:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_VALUES!r}"
    )
