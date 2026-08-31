from typing import Literal

ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_organization_products_create_catalogue_app_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
