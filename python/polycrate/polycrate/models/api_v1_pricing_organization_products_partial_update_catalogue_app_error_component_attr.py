from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_pricing_organization_products_partial_update_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
