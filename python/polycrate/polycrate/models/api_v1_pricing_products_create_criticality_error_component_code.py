from typing import Literal

ApiV1PricingProductsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_products_create_criticality_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
