from typing import Literal

ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_quotes_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
