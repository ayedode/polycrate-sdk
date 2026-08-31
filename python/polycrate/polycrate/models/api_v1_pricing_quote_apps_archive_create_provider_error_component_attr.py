from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_quote_apps_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
