from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_catalogue_app_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponentCode:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
