from typing import Literal

ApiV1PricingProductsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_PRICING_PRODUCTS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1PricingProductsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_pricing_products_list_created_by_component(value: str) -> ApiV1PricingProductsListCreatedByComponent:
    if value in API_V1_PRICING_PRODUCTS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
