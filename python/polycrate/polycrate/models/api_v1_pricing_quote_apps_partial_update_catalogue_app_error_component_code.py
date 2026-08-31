from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_quote_apps_partial_update_catalogue_app_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
