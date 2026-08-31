from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_organization_products_partial_update_active_from_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
