from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_pricing_organization_products_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
