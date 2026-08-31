from typing import Literal

ApiV1PricingProductsCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
