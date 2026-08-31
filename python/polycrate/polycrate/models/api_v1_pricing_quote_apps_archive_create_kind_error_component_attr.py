from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_quote_apps_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
