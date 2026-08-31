from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponentCode:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
