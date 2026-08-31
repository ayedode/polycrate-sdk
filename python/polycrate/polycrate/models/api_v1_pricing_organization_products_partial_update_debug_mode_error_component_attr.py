from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pricing_organization_products_partial_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
