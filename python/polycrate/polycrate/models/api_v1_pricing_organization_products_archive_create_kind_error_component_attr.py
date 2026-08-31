from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_organization_products_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
