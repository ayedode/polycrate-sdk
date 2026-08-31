from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_pricing_organization_products_archive_create_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
