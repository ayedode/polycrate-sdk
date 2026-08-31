from typing import Literal

ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_pricing_organization_products_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
