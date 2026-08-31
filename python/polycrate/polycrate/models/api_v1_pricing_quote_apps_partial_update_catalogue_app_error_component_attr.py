from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_pricing_quote_apps_partial_update_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
