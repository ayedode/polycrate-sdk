from typing import Literal

ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_PRICING_QUOTE_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_pricing_quote_apps_create_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
