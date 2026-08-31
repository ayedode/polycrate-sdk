from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_organization_products_partial_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
