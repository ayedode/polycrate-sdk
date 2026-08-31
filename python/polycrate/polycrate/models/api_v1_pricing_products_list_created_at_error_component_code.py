from typing import Literal

ApiV1PricingProductsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_PRICING_PRODUCTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_products_list_created_at_error_component_code(
    value: str,
) -> ApiV1PricingProductsListCreatedAtErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
