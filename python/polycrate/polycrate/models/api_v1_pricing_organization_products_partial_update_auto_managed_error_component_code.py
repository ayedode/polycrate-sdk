from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_organization_products_partial_update_auto_managed_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
