from typing import Literal

ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_organization_products_update_criticality_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
