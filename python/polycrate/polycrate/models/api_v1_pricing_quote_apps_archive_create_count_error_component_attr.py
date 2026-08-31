from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateCountErrorComponentAttr = Literal["count"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateCountErrorComponentAttr
] = {
    "count",
}


def check_api_v1_pricing_quote_apps_archive_create_count_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateCountErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
