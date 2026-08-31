from typing import Literal

ApiV1PricingOrganizationProductsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_organization_products_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
