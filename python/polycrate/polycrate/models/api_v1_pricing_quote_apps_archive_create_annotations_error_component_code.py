from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quote_apps_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
