from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponentAttr = Literal["active_until"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponentAttr
] = {
    "active_until",
}


def check_api_v1_pricing_organization_products_archive_create_active_until_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
