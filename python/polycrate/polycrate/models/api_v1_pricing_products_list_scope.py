from typing import Literal

ApiV1PricingProductsListScope = Literal["system", "user"]

API_V1_PRICING_PRODUCTS_LIST_SCOPE_VALUES: set[ApiV1PricingProductsListScope] = {
    "system",
    "user",
}


def check_api_v1_pricing_products_list_scope(value: str) -> ApiV1PricingProductsListScope:
    if value in API_V1_PRICING_PRODUCTS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_LIST_SCOPE_VALUES!r}")
