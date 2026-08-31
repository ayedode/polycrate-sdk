from typing import Literal

ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_organization_products_update_active_until_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
