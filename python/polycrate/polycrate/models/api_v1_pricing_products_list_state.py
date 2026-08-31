from typing import Literal

ApiV1PricingProductsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PRICING_PRODUCTS_LIST_STATE_VALUES: set[ApiV1PricingProductsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pricing_products_list_state(value: str) -> ApiV1PricingProductsListState:
    if value in API_V1_PRICING_PRODUCTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_LIST_STATE_VALUES!r}")
