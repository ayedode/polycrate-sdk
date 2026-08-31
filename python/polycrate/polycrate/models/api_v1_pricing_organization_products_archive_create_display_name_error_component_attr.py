from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_organization_products_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
