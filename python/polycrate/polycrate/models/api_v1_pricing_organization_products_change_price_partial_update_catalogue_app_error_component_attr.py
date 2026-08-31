from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponentAttr:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
