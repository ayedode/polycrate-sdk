from typing import Literal

ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_organization_products_update_auto_managed_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
