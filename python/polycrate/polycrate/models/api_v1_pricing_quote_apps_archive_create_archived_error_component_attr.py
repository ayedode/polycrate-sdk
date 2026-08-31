from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_quote_apps_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
