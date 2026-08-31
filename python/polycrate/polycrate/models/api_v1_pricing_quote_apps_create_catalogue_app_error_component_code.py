from typing import Literal

ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_QUOTE_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_quote_apps_create_catalogue_app_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
