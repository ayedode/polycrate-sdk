from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_pricing_quote_apps_archive_create_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
