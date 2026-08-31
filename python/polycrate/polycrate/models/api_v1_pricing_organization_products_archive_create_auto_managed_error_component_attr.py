from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponentAttr = Literal["auto_managed"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AUTO_MANAGED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponentAttr
] = {
    "auto_managed",
}


def check_api_v1_pricing_organization_products_archive_create_auto_managed_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AUTO_MANAGED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AUTO_MANAGED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
