from typing import Literal

ApiV1PricingProductsPartialUpdateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsPartialUpdateConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_partial_update_config_error_component_code(
    value: str,
) -> ApiV1PricingProductsPartialUpdateConfigErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
