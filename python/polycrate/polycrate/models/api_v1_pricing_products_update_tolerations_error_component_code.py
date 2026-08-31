from typing import Literal

ApiV1PricingProductsUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_update_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingProductsUpdateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
