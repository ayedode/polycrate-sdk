from typing import Literal

ApiV1PricingOrganizationProductsUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_organization_products_update_provider_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateProviderErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
