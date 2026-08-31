from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_quote_apps_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
