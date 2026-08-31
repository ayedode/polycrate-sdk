from typing import Literal

ApiV1PricingOrganizationProductsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_organization_products_update_provider_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateProviderErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
